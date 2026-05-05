## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2026-06-15 - [Accessible Navigation and Smooth State Transitions]
**Learning:** For single-page navigation, visual active states (like underlines) should be supplemented with `aria-current="location"` to ensure screen reader users are aware of their scroll position. Additionally, "Skip to content" links only work reliably if the target has `tabindex="-1"` to allow programmatic focus shifts.
**Action:** Always pair visual `.active` toggles with `aria-current` updates in scroll-spy logic, and ensure skip-link targets are focusable and have unique IDs.
