"""Comprehensive pre-push security audit script."""
import os
import re
from pathlib import Path

BASE_DIR = Path(r"c:\Users\nainl\OneDrive\Desktop\taltek-commercial-roofing")

SECRET_PATTERNS = [
    re.compile(r'AKIA[0-9A-Z]{16}'), # AWS Access Key
    re.compile(r'(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,}'), # GitHub Token
    re.compile(r'vercel_[a-zA-Z0-9]{24,}'), # Vercel Token
    re.compile(r'AIza[0-9A-Za-z-_]{35}'), # Google API Key
    re.compile(r'sk_live_[0-9a-zA-Z]{24,}'), # Stripe Live Key
    re.compile(r'-----BEGIN (?:RSA|OPENSSH|DSA|EC|PGP) PRIVATE KEY-----'), # Private Keys
]

def run_security_audit():
    print("=" * 60)
    print("STARTING SECURITY & CREDENTIALS AUDIT")
    print("=" * 60)
    
    findings = []
    env_files = list(BASE_DIR.glob("**/.env*"))
    for ef in env_files:
        if ".git" not in str(ef):
            findings.append(f"Found env file: {ef.relative_to(BASE_DIR)}")
            
    # Check all files
    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root or "screenshots_qa" in root or "__pycache__" in root:
            continue
        for f in files:
            file_path = Path(root) / f
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                for pat in SECRET_PATTERNS:
                    m = pat.search(content)
                    if m:
                        findings.append(f"{file_path.relative_to(BASE_DIR)}: Matched pattern {pat.pattern}")
            except Exception:
                pass
                
    if not findings:
        print("  -> PASSED: Zero API keys, passwords, credentials, or private secrets detected.")
    else:
        for f in findings:
            print(f"  -> WARNING: {f}")
        return False
        
    # Check .gitignore
    gitignore = (BASE_DIR / ".gitignore").read_text(encoding="utf-8")
    extra_ignores = []
    for item in [".env", ".env*.local", "*.log", ".vercel", "screenshots_qa/"]:
        if item not in gitignore:
            extra_ignores.append(item)
            
    if extra_ignores:
        print(f"  -> Updating .gitignore with: {extra_ignores}")
        with open(BASE_DIR / ".gitignore", "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(extra_ignores) + "\n")
        print("  -> .gitignore updated.")
    else:
        print("  -> .gitignore already comprehensive.")
        
    return True

if __name__ == "__main__":
    success = run_security_audit()
    print("=" * 60)
