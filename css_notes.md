# CSS Notes: From Basic to Advanced

This document provides a comprehensive guide to Cascading Style Sheets (CSS), progressing from fundamental concepts to advanced techniques. It's designed to be easy to understand, with practical examples and clear explanations.

## Table of Contents
1. [Introduction to CSS](#introduction-to-css)
2. [Basic Concepts](#basic-concepts)
3. [Selectors](#selectors)
4. [Box Model](#box-model)
5. [Layout and Positioning](#layout-and-positioning)
6. [Typography](#typography)
7. [Colors and Backgrounds](#colors-and-backgrounds)
8. [Responsive Design](#responsive-design)
9. [Animations and Transitions](#animations-and-transitions)
10. [Advanced Topics](#advanced-topics)
11. [CSS Frameworks and Preprocessors](#css-frameworks-and-preprocessors)
12. [Best Practices](#best-practices)

## Introduction to CSS

CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML or XML. It controls the layout, colors, fonts, and overall appearance of web pages.

### How CSS Works
- **Cascading**: Styles can be inherited and overridden
- **Specificity**: Determines which styles are applied when conflicts occur
- **Inheritance**: Child elements inherit styles from parent elements

### Ways to Add CSS
1. **Inline**: `<div style="color: red;">`
2. **Internal**: `<style>` tag in HTML head
3. **External**: Link to a `.css` file

## Basic Concepts

### CSS Syntax
```css
selector {
    property: value;
    another-property: another-value;
}
```

### CSS Units
- **Absolute**: px, pt, cm, mm, in
- **Relative**: %, em, rem, vw, vh, vmin, vmax

## Selectors

Selectors target HTML elements to apply styles.

### Basic Selectors
- **Element**: `p { }`
- **Class**: `.classname { }`
- **ID**: `#idname { }`
- **Universal**: `* { }`

### Combinators
- **Descendant**: `div p { }` (all p inside div)
- **Child**: `div > p { }` (direct children)
- **Adjacent Sibling**: `h1 + p { }` (next sibling)
- **General Sibling**: `h1 ~ p { }` (all siblings after)

### Attribute Selectors
- `[attribute]`: `input[type="text"]`
- `[attribute^="value"]`: starts with
- `[attribute$="value"]`: ends with
- `[attribute*="value"]`: contains

### Pseudo-classes
- `:hover`, `:focus`, `:active`
- `:first-child`, `:last-child`, `:nth-child()`
- `:not()`

### Pseudo-elements
- `::before`, `::after`
- `::first-line`, `::first-letter`

## Box Model

Every element in CSS is a rectangular box with four areas:

1. **Content**: The actual content
2. **Padding**: Space around the content
3. **Border**: A border around the padding
4. **Margin**: Space outside the border

```css
.box {
    width: 200px;
    height: 100px;
    padding: 20px;
    border: 2px solid black;
    margin: 10px;
}
```

### Box-sizing
- `content-box` (default): Width/height includes only content
- `border-box`: Width/height includes content, padding, and border

## Layout and Positioning

### Display Property
- `block`: Takes full width, stacks vertically
- `inline`: Flows with text, only takes necessary width
- `inline-block`: Inline but can have width/height
- `none`: Hides the element
- `flex`: Enables flexbox
- `grid`: Enables CSS Grid

### Position Property
- `static` (default): Normal document flow
- `relative`: Positioned relative to its normal position
- `absolute`: Positioned relative to nearest positioned ancestor
- `fixed`: Positioned relative to the viewport
- `sticky`: Toggles between relative and fixed

### Flexbox
A layout model for arranging items in a container.

```css
.container {
    display: flex;
    justify-content: center; /* horizontal alignment */
    align-items: center; /* vertical alignment */
    flex-direction: row; /* or column */
}

.item {
    flex: 1; /* grow, shrink, basis */
}
```

### CSS Grid
A two-dimensional layout system.

```css
.container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    grid-template-rows: auto;
    gap: 10px;
}
```

## Typography

### Font Properties
```css
.text {
    font-family: 'Arial', sans-serif;
    font-size: 16px;
    font-weight: bold; /* normal, bold, 100-900 */
    font-style: italic; /* normal, italic, oblique */
    line-height: 1.5;
    text-align: center; /* left, right, center, justify */
    text-decoration: underline; /* none, underline, overline, line-through */
    text-transform: uppercase; /* none, uppercase, lowercase, capitalize */
}
```

### Web Fonts
```css
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

body {
    font-family: 'Roboto', sans-serif;
}
```

## Colors and Backgrounds

### Color Values
- **Named**: `red`, `blue`, `green`
- **Hex**: `#ff0000`, `#00ff00`
- **RGB/RGBA**: `rgb(255, 0, 0)`, `rgba(255, 0, 0, 0.5)`
- **HSL/HSLA**: `hsl(0, 100%, 50%)`, `hsla(0, 100%, 50%, 0.5)`

### Background Properties
```css
.element {
    background-color: #f0f0f0;
    background-image: url('image.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover; /* auto, cover, contain, specific size */
}
```

### Gradients
```css
.linear {
    background: linear-gradient(to right, red, yellow);
}

.radial {
    background: radial-gradient(circle, red, yellow);
}
```

## Responsive Design

### Media Queries
Apply styles based on device characteristics.

```css
/* Mobile first */
@media (min-width: 768px) {
    .container {
        width: 750px;
    }
}

@media (min-width: 992px) {
    .container {
        width: 970px;
    }
}
```

### Flexible Images
```css
img {
    max-width: 100%;
    height: auto;
}
```

### Viewport Meta Tag
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Animations and Transitions

### Transitions
Smooth changes between states.

```css
.button {
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: blue;
}
```

### Keyframe Animations
```css
@keyframes slideIn {
    from {
        transform: translateX(-100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

.element {
    animation: slideIn 1s ease-in-out;
}
```

### Transform Property
```css
.element {
    transform: rotate(45deg);
    transform: scale(1.2);
    transform: translate(50px, 100px);
    transform: skew(10deg, 20deg);
}
```

## Advanced Topics

### CSS Variables (Custom Properties)
```css
:root {
    --primary-color: #007bff;
    --font-size: 16px;
}

.element {
    color: var(--primary-color);
    font-size: var(--font-size);
}
```

### CSS Functions
- `calc()`: `width: calc(100% - 20px);`
- `min()`, `max()`, `clamp()`: `font-size: clamp(1rem, 2vw, 2rem);`
- `attr()`: Access HTML attributes

### CSS Shapes
```css
.shape {
    shape-outside: circle(50%);
    clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}
```

### CSS Filters
```css
.image {
    filter: blur(5px);
    filter: brightness(1.2);
    filter: contrast(120%);
    filter: grayscale(50%);
}
```

### CSS Counters
```css
ol {
    counter-reset: section;
}

li::before {
    counter-increment: section;
    content: counter(section) ". ";
}
```

## CSS Frameworks and Preprocessors

### Popular Frameworks
- **Bootstrap**: Responsive grid system, components
- **Tailwind CSS**: Utility-first CSS framework
- **Bulma**: Modern CSS framework based on Flexbox

### CSS Preprocessors
- **Sass/SCSS**: Variables, nesting, mixins, functions
- **Less**: Similar to Sass but with JavaScript integration
- **Stylus**: Expressive syntax

Example Sass:
```scss
$primary-color: #007bff;

.button {
    background-color: $primary-color;
    
    &:hover {
        background-color: darken($primary-color, 10%);
    }
}
```

## Best Practices

### Organization
- Use consistent naming conventions (BEM, SMACSS)
- Group related styles together
- Use comments to organize code

### Performance
- Minimize CSS file size
- Use CSS sprites for multiple images
- Avoid deep selector chains
- Use `will-change` for animated properties

### Maintainability
- Use CSS variables for reusable values
- Avoid `!important` unless necessary
- Keep specificity low
- Use shorthand properties

### Accessibility
- Ensure sufficient color contrast
- Don't rely solely on color for meaning
- Test with keyboard navigation
- Use semantic HTML with appropriate styles

### Cross-browser Compatibility
- Use vendor prefixes when necessary
- Test on multiple browsers
- Use tools like Autoprefixer
- Keep up with browser support tables

This comprehensive guide covers the essential aspects of CSS from beginner to advanced levels. Practice regularly by building projects and experimenting with different techniques. CSS is constantly evolving, so stay updated with the latest specifications and browser capabilities.
