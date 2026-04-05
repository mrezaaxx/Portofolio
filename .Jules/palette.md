## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-25 - [Navigation and Keyboard Accessibility Polish]
**Learning:** For single-page portfolios, combining a 'Skip to content' link with standardized 'focus-visible' outlines (using a 4px offset) drastically improves keyboard navigation. Additionally, an IntersectionObserver with a 'rootMargin' of '-50% 0px' provides the most natural 'active' link highlighting for users as they scroll through vertical sections.
**Action:** Always include a 'Skip to' link as the first body child and use high-contrast focus indicators with offsets to ensure accessibility without compromising the aesthetic.
