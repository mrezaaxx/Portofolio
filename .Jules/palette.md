## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2026-05-15 - [Aria-current and Focus Management for SPAs]
**Learning:** For single-page applications using scroll-spy, visual highlighting alone is insufficient for accessibility. Using 'aria-current="location"' on active navigation links ensures screen reader users are informed of their current position. Additionally, when using skip-to-content links, the target container must have 'tabindex="-1"' to ensure reliable focus shifting across all browsers.
**Action:** Always pair visual 'active' classes with 'aria-current="location"' in scroll-spy implementations, and ensure skip-link targets are programmatically focusable using 'tabindex="-1"'.
