#!/usr/bin/env python3
"""Zero-Trust Verification for Architecture Tools Landing Page"""

import json
from playwright.sync_api import sync_playwright

URL = "http://localhost:8765/index.html"
RESULTS = {
    "console_errors": [],
    "checks": []
}

def add_check(name, passed, details=""):
    RESULTS["checks"].append({
        "name": name,
        "passed": passed,
        "details": details
    })
    status = "✅" if passed else "❌"
    print(f"{status} {name}: {details}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Collect console errors
        page.on("console", lambda msg: RESULTS["console_errors"].append(msg.text) if msg.type == "error" else None)

        print("\n=== ZERO-TRUST VERIFICATION: Landing Page ===\n")

        # Load page
        response = page.goto(URL, wait_until="networkidle")
        add_check("Page loads", response.status == 200, f"HTTP {response.status}")

        # Wait for fonts and images
        page.wait_for_timeout(2000)

        # === SECTION 1: Element Visibility ===
        print("\n--- Element Visibility ---")

        # Hero section
        hero = page.locator(".hero").first
        hero_box = hero.bounding_box()
        add_check("Hero section visible", hero_box and hero_box["height"] > 0, f"height={hero_box['height'] if hero_box else 0}px")

        # Brand label
        brand = page.locator(".brand-label").first
        brand_visible = brand.is_visible()
        brand_text = brand.text_content()
        add_check("Brand label visible", brand_visible and "WEAVER" in brand_text.upper(), f"text='{brand_text}'")

        # Hero title
        title = page.locator(".hero-title").first
        title_visible = title.is_visible()
        title_text = title.text_content()
        add_check("Hero title visible", title_visible and "Architecture" in title_text, f"contains 'Architecture'")

        # Hero image
        hero_img = page.locator(".hero-image").first
        img_box = hero_img.bounding_box()
        add_check("Hero image dimensions > 0", img_box and img_box["width"] > 0 and img_box["height"] > 0,
                  f"{img_box['width']:.0f}x{img_box['height']:.0f}px" if img_box else "0x0")

        # IRC section
        irc = page.locator(".irc-section").first
        irc_box = irc.bounding_box()
        add_check("IRC section visible", irc_box and irc_box["height"] > 0, f"height={irc_box['height'] if irc_box else 0}px")

        # IRC link
        irc_link = page.locator(".irc-link").first
        link_href = irc_link.get_attribute("href")
        add_check("IRC link points to stairs.html", link_href == "stairs.html", f"href='{link_href}'")

        # === SECTION 2: Design Token Verification ===
        print("\n--- Design Token Verification ---")

        # Check primary color on brand label
        brand_color = page.evaluate("""() => {
            const el = document.querySelector('.brand-label');
            return getComputedStyle(el).color;
        }""")
        # #2C4C3B = rgb(44, 76, 59)
        add_check("Brand label uses primary color", "44, 76, 59" in brand_color or "2c4c3b" in brand_color.lower(),
                  f"color={brand_color}")

        # Check background color
        bg_color = page.evaluate("""() => {
            return getComputedStyle(document.body).backgroundColor;
        }""")
        # #FDFBF7 = rgb(253, 251, 247)
        add_check("Body uses background token", "253, 251, 247" in bg_color or "fdfbf7" in bg_color.lower(),
                  f"bg={bg_color}")

        # Check IRC section background
        irc_bg = page.evaluate("""() => {
            const el = document.querySelector('.irc-section');
            return getComputedStyle(el).backgroundColor;
        }""")
        add_check("IRC section uses primary background", "44, 76, 59" in irc_bg or "2c4c3b" in irc_bg.lower(),
                  f"bg={irc_bg}")

        # Check serif font on title
        title_font = page.evaluate("""() => {
            const el = document.querySelector('.hero-title');
            return getComputedStyle(el).fontFamily;
        }""")
        add_check("Hero title uses serif font", "playfair" in title_font.lower() or "serif" in title_font.lower(),
                  f"font={title_font[:50]}...")

        # === SECTION 3: Interactive States ===
        print("\n--- Interactive States ---")

        # Hero image grayscale filter
        img_filter_before = page.evaluate("""() => {
            const el = document.querySelector('.hero-image');
            return getComputedStyle(el).filter;
        }""")
        add_check("Hero image has grayscale filter", "grayscale" in img_filter_before, f"filter={img_filter_before}")

        # Hover on hero image container
        hero_container = page.locator(".hero-image-container").first
        hero_container.hover()
        page.wait_for_timeout(800)  # Wait for transition

        img_filter_after = page.evaluate("""() => {
            const el = document.querySelector('.hero-image');
            return getComputedStyle(el).filter;
        }""")
        # After hover, grayscale should be 0% or none
        grayscale_removed = "grayscale(0" in img_filter_after or img_filter_after == "none"
        add_check("Hover removes grayscale", grayscale_removed, f"filter after hover={img_filter_after}")

        # === SECTION 4: Responsive Layout ===
        print("\n--- Layout Check ---")

        # Check two-column layout on desktop
        hero_content = page.locator(".hero-content").first
        hero_content_style = page.evaluate("""() => {
            const el = document.querySelector('.hero-content');
            return {
                display: getComputedStyle(el).display,
                flexDirection: getComputedStyle(el).flexDirection
            };
        }""")
        is_flex = hero_content_style["display"] == "flex"
        add_check("Hero uses flex layout", is_flex, f"display={hero_content_style['display']}")

        # === SECTION 5: Console Errors ===
        print("\n--- Console Errors ---")

        # Filter out favicon errors
        real_errors = [e for e in RESULTS["console_errors"] if "favicon" not in e.lower()]
        add_check("Zero console errors", len(real_errors) == 0,
                  f"{len(real_errors)} errors" if real_errors else "clean")
        if real_errors:
            for err in real_errors:
                print(f"   ⚠️ {err}")

        # === SECTION 6: Link Navigation ===
        print("\n--- Link Navigation ---")

        # Test IRC link navigates correctly
        irc_link.click()
        page.wait_for_load_state("networkidle")
        current_url = page.url
        add_check("IRC link navigates to stairs.html", "stairs.html" in current_url, f"url={current_url}")

        # Check stairs page loaded
        stairs_title = page.title()
        add_check("Stairs page loads", "stair" in stairs_title.lower(), f"title='{stairs_title}'")

        browser.close()

        # === SUMMARY ===
        print("\n=== VERIFICATION SUMMARY ===")
        passed = sum(1 for c in RESULTS["checks"] if c["passed"])
        total = len(RESULTS["checks"])
        print(f"\nPassed: {passed}/{total}")

        if passed == total:
            print("\n✅ ALL CHECKS PASSED")
        else:
            print("\n❌ SOME CHECKS FAILED")
            for c in RESULTS["checks"]:
                if not c["passed"]:
                    print(f"   - {c['name']}: {c['details']}")

        return passed == total

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
