## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-24 - [Accessible & Context-Aware Navigation]
**Learning:** For single-page portfolios, accessibility (Skip to content) and visual feedback (Scroll Spy) must work together. A skip link improves keyboard efficiency, while Scroll Spy provides essential context for where the user is in the long-scrolling document.
**Action:** Always pair jump-links with clear `:focus-visible` styles and IntersectionObserver-based active states to create a cohesive navigation experience for all users.
