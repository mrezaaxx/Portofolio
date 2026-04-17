## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-25 - [Accessibility & Navigation Enhancements]
**Learning:** Combining a "Skip to content" link with a scroll-spy navigation provides a seamless experience for both keyboard and mouse users. Adding ARIA labels and semantic roles to icon-only elements (like emojis) is a critical micro-UX win that makes the portfolio truly inclusive for screen reader users. Standardizing focus indicators with `*:focus-visible` ensures that keyboard navigation is always visually clear without cluttering the UI for mouse users.
**Action:** Always include a skip link for single-page applications and ensure interactive icons are wrapped in semantic tags with ARIA labels. Use `IntersectionObserver` with a centered `rootMargin` for more natural scroll-spy highlighting.
