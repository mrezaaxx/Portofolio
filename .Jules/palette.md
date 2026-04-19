## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-19 - [Accessibility Foundation for Single-Page Portfolios]
**Learning:** For single-page portfolios with interactive elements and scroll-based navigation, a "Skip to content" link and explicit `:focus-visible` styles are essential foundations that dramatically improve keyboard navigation. Adding `tabindex="-1"` to the target section ensures that the skip link correctly moves focus, not just the scroll position. Wrapping emojis in `role="img"` with `aria-label` provides necessary context for screen readers in icon-heavy layouts.
**Action:** Always include a skip-link and `:focus-visible` styles as a first step when improving the accessibility of a static landing page or portfolio.
