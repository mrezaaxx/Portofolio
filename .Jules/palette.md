## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2026-06-19 - [Navigation & Scroll UX Polish]
**Learning:** Consolidating redundant accessibility styles in a single-file portfolio prevents style drift and ensures a consistent keyboard navigation experience. Using `scroll-padding-top` is a cleaner, CSS-only solution for fixed headers than adding invisible offset elements or manual JS scroll offsets. Avoid `letter-spacing` transitions on navigation elements as they cause jittery layout shifts.
**Action:** Always check for redundant style blocks in large HTML files before adding new ones. Use `scroll-padding-top` on the `html` element for all sticky/fixed navigation layouts.
