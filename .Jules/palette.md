## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2026-05-15 - [Descriptive ARIA labels for progress bars]
**Learning:** Progress bars (role="progressbar") without an accessible name are incomplete for screen reader users. Deriving an aria-label from nearby semantic text (like a skill name span) ensures that users with visual impairments understand exactly what the metric represents without visual context.
**Action:** Always provide an 'aria-label' or 'aria-labelledby' for elements with the 'progressbar' role to specify the category being measured.

## 2026-05-15 - [Accessible emoji handling]
**Learning:** Raw emojis in HTML can be confusing for screen readers as they read out the default emoji metadata (e.g., "round pushpin"). Wrapping them in a span with role="img" and a descriptive aria-label (e.g., "Location") provides immediate semantic clarity.
**Action:** Wrap all informative emojis in '<span role="img" aria-label="..."></span>' to ensure they are accessible and meaningful to assistive technologies.
