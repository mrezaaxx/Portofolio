## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2026-05-15 - [Dynamic ARIA injection for repeated elements]
**Learning:** In repositories with strict line-count limits (e.g., 50-line diffs), adding accessibility attributes like `aria-label` to dozens of repeated elements (like skill bars) is best handled via a small JavaScript loop. This maintains a clean diff while significantly improving screen reader support.
**Action:** Use `document.querySelectorAll().forEach()` to inject contextual `aria-label` attributes derived from sibling text elements for repeated decorative UI components.

## 2026-05-15 - [Accessible Scroll-Spy with aria-current]
**Learning:** Visual-only active states in navigation (e.g., `.active` class) are insufficient for accessibility. Toggling `aria-current="location"` in sync with the scroll-spy observer ensures that screen reader users are informed of their current position within the single-page application.
**Action:** Always pair visual active classes in navigation with `aria-current="location"` when using IntersectionObservers for scroll-spy functionality.
