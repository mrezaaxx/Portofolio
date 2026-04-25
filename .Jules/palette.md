## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2026-10-27 - [Consolidated accessibility styles and unique main-content ID]
**Learning:** In long, single-file HTML projects, accessibility boilerplate (like skip-links and focus indicators) can often become redundant or duplicated during rapid development. Duplicate IDs, particularly for the skip-link target, break navigation for keyboard/screen-reader users. Consolidating these styles and ensuring ID uniqueness is a critical micro-UX fix.
**Action:** Always audit for duplicate IDs using `document.querySelectorAll('[id]')` and consolidate global accessibility CSS into a single dedicated block to maintain consistency and prevent broken skip-to-content links.
