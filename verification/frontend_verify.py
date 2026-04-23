import os
from playwright.sync_api import sync_playwright

def run_cuj(page):
    file_path = f"file://{os.path.abspath('index.html')}"
    page.goto(file_path)
    page.wait_for_timeout(1000)

    # 1. Skip Link CUJ
    print("Testing Skip Link...")
    page.keyboard.press("Tab")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/skip_link_visible.png")

    # 2. Scroll-Spy CUJ
    print("Testing Scroll-Spy...")
    sections = ["projects", "skills", "about"]
    for section_id in sections:
        print(f"Scrolling to {section_id}...")
        section = page.locator(f"#{section_id}")
        section.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path=f"/home/jules/verification/screenshots/scroll_spy_{section_id}.png")

    page.wait_for_timeout(1000)
    # Final state
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
