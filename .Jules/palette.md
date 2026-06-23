## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2026-06-23 - [Accessibility for decorative and functional micro-interactions]
**Learning:** Even small decorative elements like location emojis (📍) should be wrapped in semantic spans with ARIA roles/labels to prevent screen readers from reading literal emoji names that lack context. Additionally, functional links like a logo linking to "#" should have explicit ARIA labels (e.g., "Back to top") to guide assistive technology users.
**Action:** Always wrap emojis in `<span role="img" aria-label="...">` and provide clear `aria-label` for navigation elements that rely on brand identity or icons for visual communication.
