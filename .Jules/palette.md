## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-24 - [Enhancing Single-Page Navigation and A11y]
**Learning:** Combining a "Skip to content" link with a performant Scroll-Spy (via IntersectionObserver) and semantic landmarks (`<main>`, `aria-label`) creates a significantly more professional and accessible single-page portfolio experience for both keyboard and screen reader users.
**Action:** Always include a Skip Link and standardized `:focus-visible` styles when refining static portfolios, and use a `-50%` rootMargin for Scroll-Spy to ensure the transition happens at the viewport midpoint.
