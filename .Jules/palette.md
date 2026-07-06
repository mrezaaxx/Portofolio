## 2025-05-24 - [Scroll-triggered animations for skill bars]
**Learning:** Adding scroll-triggered animations to static elements like skill bars provides a professional "touch of delight" that makes a portfolio feel more dynamic and polished without affecting core functionality. Using IntersectionObserver is the most performant way to implement this as it avoids continuous scroll event listeners.
**Action:** When implementing progressive disclosure or animations, use IntersectionObserver to trigger them only when they enter the viewport and unobserve immediately after the animation starts to save resources.

## 2026-04-03 - [Scroll-Spy for single-page navigation]
**Learning:** For single-page portfolios, a scroll-spy implementation using IntersectionObserver with rootMargin: '0px 0px -50% 0px' provides a more natural feel for active link highlighting than a simple threshold, as it triggers when a section crosses the horizontal midline of the viewport.
**Action:** Use rootMargin with a negative bottom value (e.g., -50%) for scroll-spy to ensure the active state changes precisely when the user has scrolled significantly into the next section.

## 2026-06-21 - [Programmatic Accessibility Injection]
**Learning:** For repositories with many repeated elements and strict diff limits (e.g., 50 lines), programmatically injecting ARIA attributes via JavaScript is a highly efficient way to improve accessibility. This approach ensures all relevant elements are covered while keeping the codebase clean and the diff surgical.
**Action:** When faced with a large number of elements requiring similar accessibility enhancements, use a small JavaScript loop to inject attributes like `aria-label` or `role`. Ensure the script is robust by including null safety checks for source elements and string sanitization (like `.trim()`).
