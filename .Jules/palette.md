## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-24 - [Accessible Navigation and Focus States]
**Learning:** For single-page portfolios, combining a 'Skip to content' link with semantic section IDs and explicit ':focus-visible' styles significantly improves keyboard navigability. Highlighting active sections in the nav via 'IntersectionObserver' (Scroll-Spy) provides essential visual context for all users, making the navigation feel responsive to their position.
**Action:** Always include a 'Skip to content' link as the first focusable element and use ':focus-visible' for consistent, accessible focus indicators that don't distract mouse users.
