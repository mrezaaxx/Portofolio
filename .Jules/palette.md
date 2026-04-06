## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-24 - [Accessibility and Navigation Polish]
**Learning:** Combining scroll-spy navigation with accessible focus states and skip links significantly improves the usability of single-page portfolios for both mouse and keyboard users. Using IntersectionObserver with a specific `rootMargin` (e.g., `'0px 0px -50% 0px'`) ensures the active nav state updates accurately as the user crosses section boundaries.
**Action:** For every single-page layout, proactively implement skip-to-content links and standardized `:focus-visible` states to ensure universal accessibility from the start.
