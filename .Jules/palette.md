## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-24 - [Accessibility and Navigation Enhancements]
**Learning:** For single-page portfolios, combining a "Skip to content" link, clear focus indicators, and a scroll-spy navigation provides a significantly improved experience for both power users and users with accessibility needs. Scroll-spy requires careful tuning of IntersectionObserver's rootMargin to ensure the active state transitions at a natural point (e.g., when the section reaches the middle of the viewport).
**Action:** Always include a skip link and focus-visible states. When using scroll-spy, ensure all sections have unique IDs and use a rootMargin like '0px 0px -50% 0px' for accurate detection.
