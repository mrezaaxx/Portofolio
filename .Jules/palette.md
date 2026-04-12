## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-25 - [Accessibility Pass: Skip Link and Focus States]
**Learning:** In minimal, dark-themed portfolios, keyboard navigation can easily be overlooked. A "Skip to content" link and global `*:focus-visible` indicators are essential micro-UX additions that significantly improve accessibility without cluttering the visual design for mouse users.
**Action:** Always include a skip link and clear focus-visible states as part of the baseline accessibility pass for any UI.
