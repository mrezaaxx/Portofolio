## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-25 - [Combining Navigation Feedback and Accessibility]
**Learning:** For single-page portfolios, navigation feedback (Scroll-Spy) and keyboard accessibility (Skip-to-content links, standardized focus indicators) are foundational UX elements. Implementing them together ensures that both mouse and keyboard users have a clear understanding of their current context and can navigate efficiently. IntersectionObserver with a rootMargin of '0px 0px -50% 0px' provides a robust "active" state that matches user expectation.
**Action:** Always include skip-to-content links and high-contrast focus indicators alongside interactive navigation elements to ensure WCAG compliance and improved UX for all users.
