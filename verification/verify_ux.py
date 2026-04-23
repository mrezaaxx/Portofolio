import os
import asyncio
from playwright.async_api import async_playwright

async def verify_ux():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Use absolute path for file:// protocol
        file_path = f"file://{os.path.abspath('index.html')}"
        page = await browser.new_page()
        await page.goto(file_path)

        print("Testing Skip Link...")
        skip_link = page.locator(".skip-link")
        await page.keyboard.press("Tab")
        # Check if skip link is focused and visible (top: 0)
        is_focused = await skip_link.evaluate("el => document.activeElement === el")
        # Give it a moment for transition
        await asyncio.sleep(0.5)
        top_value_px = await skip_link.evaluate("el => parseFloat(getComputedStyle(el).top)")

        if is_focused and abs(top_value_px) < 1:
            print("✅ Skip link focused and visible on Tab.")
        else:
            print(f"❌ Skip link focus/visibility failed. Focused: {is_focused}, Top: {top_value_px}px")

        print("Testing Scroll-Spy and ARIA-current...")
        # Scroll to Projects section
        projects_section = page.locator("#projects")
        await projects_section.scroll_into_view_if_needed()
        # Small wait for IntersectionObserver
        await asyncio.sleep(0.5)

        projects_link = page.locator('.nav-links a[href="#projects"]')
        is_active = await projects_link.evaluate("el => el.classList.contains('active')")
        aria_current = await projects_link.get_attribute("aria-current")

        if is_active and aria_current == "location":
            print("✅ Projects link marked as active and aria-current='location'.")
        else:
            print(f"❌ Projects link state failed. Active: {is_active}, aria-current: {aria_current}")

        # Scroll back to hero (main-content target)
        await page.evaluate("window.scrollTo(0, 0)")
        await asyncio.sleep(0.5)

        # Verify nav label
        nav = page.locator("nav")
        nav_label = await nav.get_attribute("aria-label")
        if nav_label == "Main Navigation":
            print("✅ Nav has correct aria-label.")
        else:
            print(f"❌ Nav aria-label missing or incorrect: {nav_label}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_ux())
