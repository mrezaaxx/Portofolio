## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-24 - [Standardized Focus and Scroll-Spy]
**Learning:** For dark-themed minimalist portfolios, a bold `*:focus-visible` outline using the primary accent color with a generous `outline-offset` (4px) significantly improves keyboard discoverability without cluttering the visual design for mouse users. Additionally, a robust scroll-spy using `IntersectionObserver` with a `rootMargin` of `0px 0px -50% 0px` ensures that the active navigation state accurately reflects what the user is actually reading in the middle of the screen.
**Action:** Always implement global focus-visible states and use centered IntersectionObserver margins for accurate single-page navigation tracking.
