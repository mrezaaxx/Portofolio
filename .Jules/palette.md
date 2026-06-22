## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2025-06-22 - [Enhancing Sticky Header Navigation and Scroll-Spy ARIA]
**Learning:** For single-page applications with fixed headers, 'scroll-padding-top' is essential to prevent the header from obscuring section headings during anchor navigation. Furthermore, dynamically managing 'aria-current="location"' on navigation links via IntersectionObserver significantly improves the experience for screen reader users by providing real-time feedback on their location within the page.
**Action:** Always verify header height and apply matching 'scroll-padding-top' to the 'html' element. Ensure that active navigation states are reflected in the accessibility tree using 'aria-current'.
