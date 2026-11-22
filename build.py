"""
TALTEK COMMERCIAL ROOFING - MASTER BUILD PIPELINE
Runs the complete asset and page generation pipeline end-to-end.
"""

import sys
import time

def run_pipeline():
    start_time = time.time()
    print("=" * 60)
    print("STARTING TALTEK COMMERCIAL ROOFING FULL BUILD PIPELINE")
    print("=" * 60)

    try:
        # 1. Build templates
        import build_templates
        print("[1/9] Base templates loaded successfully.")

        # 2. Generate vector assets
        import generate_assets
        print("[2/9] Vector assets generated successfully.")

        # 3. Generate Southeast map and technical diagrams
        import generate_more_assets
        print("[3/9] Southeast map & technical diagrams generated successfully.")

        # 4. Generate index.html
        from generate_home import build_home
        build_home()
        print("[4/9] index.html generated successfully.")

        # 5. Generate service pages
        from generate_services import build_services_overview, build_individual_services
        build_services_overview()
        build_individual_services()
        print("[5/9] All 13 service pages generated successfully.")

        # 6. Generate project portfolio and case studies
        from generate_projects import build_projects_index, build_case_studies
        build_projects_index()
        build_case_studies()
        print("[6/9] Project portfolio and 5 case studies generated successfully.")

        # 7. Generate interactive tool pages
        from generate_tools import build_estimator_page, build_quote_page, build_financing_page, build_service_areas_page
        build_estimator_page()
        build_quote_page()
        build_financing_page()
        build_service_areas_page()
        print("[7/9] All 4 dedicated functional tool pages generated successfully.")

        # 8. Generate corporate company pages
        from generate_company import build_about_page, build_team_page, build_faq_page, build_careers_page, build_contact_page
        build_about_page()
        build_team_page()
        build_faq_page()
        build_careers_page()
        build_contact_page()
        print("[8/9] All 5 corporate company pages generated successfully.")

        # 9. Generate legal & privacy pages
        from generate_legal import (
            build_privacy_policy, build_cookie_policy, build_terms_page,
            build_accessibility_page, build_california_privacy,
            build_privacy_request_page, build_sms_terms_page
        )
        build_privacy_policy()
        build_cookie_policy()
        build_terms_page()
        build_accessibility_page()
        build_california_privacy()
        build_privacy_request_page()
        build_sms_terms_page()
        print("[9/9] All 7 legal and privacy compliance pages generated successfully.")

        # 10. Generate SEO metadata & server
        import generate_seo_and_server
        print("[SUCCESS] SEO metadata and server files generated.")

        elapsed = time.time() - start_time
        print("=" * 60)
        print(f"BUILD COMPLETED IN {elapsed:.2f} SECONDS WITH ZERO ERRORS!")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"\n[FATAL ERROR IN BUILD PIPELINE]: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = run_pipeline()
    if not success:
        sys.exit(1)
