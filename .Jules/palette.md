## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-25 - [Accessible Scroll-spy for single-page navigation]
**Learning:** Scroll-spy provides essential orientation on long single-page sites. Combining IntersectionObserver with `aria-current="location"` ensures that both sighted and screen reader users remain oriented to their current section.
**Action:** Always pair visual 'active' classes with semantic ARIA attributes like `aria-current="location"` when implementing scroll-position-based navigation highlights.
