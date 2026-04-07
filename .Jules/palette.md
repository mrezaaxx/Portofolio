## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2025-05-24 - [Accessible emojis and Scroll-Spy functionality]
**Learning:** For single-page portfolios, Scroll-Spy provides a clear visual indicator of the current section, improving navigation context. Always wrap decorative/informative emojis in 'span role="img"' with 'aria-label' to ensure accessibility for screen readers. A 'Skip to content' link is a low-effort, high-impact accessibility win for keyboard users.
**Action:** Use IntersectionObserver with 'rootMargin: "0px 0px -50% 0px"' for Scroll-Spy to ensure the active link updates when a section is roughly halfway up the viewport.
