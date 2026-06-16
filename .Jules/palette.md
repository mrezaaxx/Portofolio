## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2025-05-25 - [Accessible Emojis and Valid HTML Structure]
**Learning:** Decorative and informative emojis (like 📍 for location) should be wrapped in a span with `role="img"` and `aria-label` to ensure they are properly announced by screen readers. Additionally, duplicate IDs (like `main-content`) can break critical accessibility features like skip-to-content links.
**Action:** Always wrap stand-alone emojis in accessible spans and ensure that target IDs for skip-links are unique within the DOM.
