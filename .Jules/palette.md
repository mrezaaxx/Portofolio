## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-02 - [Scroll-spy and Keyboard Focus states]
**Learning:** For single-page portfolios, scroll-spy combined with clear keyboard focus indicators creates a much more cohesive and accessible experience. An `IntersectionObserver` with `rootMargin: '0px 0px -50% 0px'` is ideal for scroll-spy as it triggers the change when a section is roughly in the center of the viewport, which feels most natural to users.
**Action:** Always provide a high-contrast `:focus-visible` state for keyboard navigation. For scroll-spy, use an observer that tracks sections and toggles an `.active` class on corresponding navigation links.
