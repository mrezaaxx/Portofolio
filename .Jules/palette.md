## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2026-06-28 - [Accessibility-enhanced Scroll-Spy and Navigation]
**Learning:** For single-page applications, a scroll-spy should not only update visual classes but also semantic attributes like `aria-current="location"` to inform screen reader users of their current position. Additionally, ensure the skip-to-content target has `tabindex="-1"` and a unique ID to guarantee reliable focus management across different browsers.
**Action:** Always pair visual 'active' state changes with the `aria-current` attribute in scroll-spy implementations and verify skip-link targets for both uniqueness and focusability.
