## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-25 - [IntersectionObserver for Scroll-Spy Accuracy]
**Learning:** When implementing a scroll-spy for single-page navigation, standard IntersectionObserver thresholds can lead to multiple sections being 'active' or laggy highlighting. A rootMargin of `0px 0px -50% 0px` combined with a low threshold (`0.1`) ensures only the section occupying the top half of the viewport triggers the navigation highlight.
**Action:** Use a negative bottom rootMargin for scroll-spy observers to 'tighten' the detection area to the top half of the screen, providing more intuitive navigation feedback.
