## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-24 - [Accessibility Baseline for Single-Page Portfolios]
**Learning:** Single-page portfolios often lack essential accessibility features like skip links and landmark structures, which are critical for keyboard and screen reader users. Additionally, decorative elements (like emojis) should be hidden to reduce screen reader noise, and color contrast should be verified for all text states.
**Action:** Always include a "Skip to content" link, wrap main content in a `<main>` tag, and use ARIA roles (like `progressbar`) for visual-only data representations to ensure a baseline level of accessibility.
