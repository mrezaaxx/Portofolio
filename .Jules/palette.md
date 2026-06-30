## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2024-06-05 - [Accessible Emojis and Scroll Padding]
**Learning:** Decorative or informative emojis like location pins (📍) should be wrapped in semantic spans with ARIA roles and labels to ensure screen readers provide context. Additionally, for single-page apps with fixed headers, 'scroll-padding-top' is essential to prevent content from being obscured during anchor navigation.
**Action:** Always check for raw emojis and ensure they are accessible. Include 'scroll-padding-top' whenever a fixed navigation header is present.
