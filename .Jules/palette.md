## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2024-04-24 - [Accessible Scroll-Spy with ARIA]
**Learning:** For single-page navigation, visual active states (.active class) are insufficient for screen readers. Toggling the 'aria-current="location"' attribute on navigation links during scroll-spy updates ensures that assistive technologies can correctly identify and announce the current section to the user.
**Action:** Always pair visual active classes with semantic ARIA attributes like 'aria-current' in scroll-spy implementations to maintain parity between the visual and accessible experience.
