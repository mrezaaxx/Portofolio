## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2024-05-25 - [Multi-faceted Navigation & Accessibility Polish]
**Learning:** For single-page applications with fixed headers, three critical UX/a11y patterns are often missed: 1) `scroll-padding-top` to prevent header overlap, 2) Ensuring ID uniqueness for skip-links, and 3) Synchronizing `aria-current="location"` with scroll-spy state.
**Action:** Always verify that fixed headers have corresponding `scroll-padding-top` and that any "Skip to Content" targets are unique and correctly located at the start of the main landmark.
