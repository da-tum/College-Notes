# Web Development Lab 3: Portfolio Website

## Overview

This project implements a responsive portfolio website as part of Web Development Lab 3. The website showcases proficiency in HTML5 semantic markup and CSS3 styling, incorporating modern web development techniques such as animations, transitions, and responsive design principles.

## Features

- **Semantic HTML5 Structure**: Utilizes elements including `<header>`, `<section>`, `<nav>`, `<form>`, and `<footer>` for accessible and structured content.
- **CSS3 Styling and Layout**: Employs CSS Grid and Flexbox for layout management, CSS custom properties for theming, and media queries for responsive behavior.
- **Animations and Interactions**: Implements keyframe animations for visual effects and CSS transitions for hover states.
- **Responsive Design**: Ensures optimal viewing across devices with mobile-first breakpoints.

## File Structure

- `index.html`: Primary HTML document containing the website's markup.
- `style.css`: Comprehensive stylesheet defining all visual styles, animations, and responsive rules.

## Key Technologies and Techniques

### HTML5 Elements
- Structural elements: `<header>`, `<section>`, `<footer>`
- Interactive elements: `<nav>`, `<form>`, `<input>`, `<textarea>`
- Media elements: `<img>`

### CSS3 Techniques
- Layout: Grid and Flexbox
- Theming: CSS custom properties (variables)
- Animations: `@keyframes` for fade effects
- Interactions: `transform`, `transition`, and `box-shadow` for hover effects
- Responsiveness: Media queries for adaptive layouts

## Code Examples

### CSS Grid Layout
```css
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
}
```

### Keyframe Animation
```css
@keyframes fade-in {
  0%, 100% { opacity: 0; }
  50% { opacity: 1; }
}
```

## Installation and Usage

1. Clone the repository or download the project files.
2. Open `index.html` in a modern web browser.
3. Navigate through the sections: Hero, Skills, Projects, and Contact.

No additional dependencies or server setup is required, as this is a static website.

## Technologies Used

- HTML5
- CSS3
