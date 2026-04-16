## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-24 - [Accessible Navigation and Keyboard Visibility]
**Learning:** Single-page portfolios often overlook keyboard navigation. Adding a 'Skip to content' link and standardizing focus indicators with `*:focus-visible` ensures that the site is navigable for all users without cluttering the UI for mouse users. Combining this with a scroll-spy using `IntersectionObserver` provides both accessibility and a polished interactive feel.
**Action:** Always include a skip link and explicit focus-visible states in single-page applications. Use IntersectionObserver with a negative rootMargin (e.g., `0px 0px -50% 0px`) for accurate scroll-spy tracking.
