# CLAUDE.md

This file provides guidance to Claude Code and other AI coding assistants when working with this repository.

## Project Overview

**Architecture Tools** - A collection of vibe-coded tools for architectural practice. Built with web technologies and integrated with the M3 Design System v2.

## Design System Integration

This project uses components from the **M3 Design System v2** located at:
`/Users/mwy/Library/Mobile Documents/com~apple~CloudDocs/Projects/m3-design-v2`

### Key Principles

1. **Use design system components** (`wy-*` web components) whenever possible
2. **Use design tokens** from the design system for colors, spacing, typography
3. **Never hardcode values** - always reference CSS custom properties
4. **Follow the Soft Modernism aesthetic**: organic M3 shapes + editorial typography + warm heritage palette

### Consuming the Design System

```html
<!-- Load design tokens -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/wyyew/m3-design-v2@main/src/styles/tokens.css">

<!-- Load web components -->
<script type="module" src="https://cdn.jsdelivr.net/gh/wyyew/m3-design-v2@main/dist/web-components.js"></script>
```

### Design Tokens Reference

**Colors:**
- `--md-sys-color-primary`: #2C4C3B (Hunter Green)
- `--md-sys-color-background`: #FDFBF7 (Alabaster)
- `--md-sys-color-surface`: #F5F2EA (Warm Clay)
- `--md-sys-color-on-surface`: #121714

**Typography:**
- Headings: `var(--font-serif)` (Playfair Display)
- Body/UI: `var(--font-sans)` (DM Sans)
- Labels: ALL CAPS with `letter-spacing: 0.05em-0.1em`

**Spacing (8px baseline):**
- `--spacing-xs`: 4px
- `--spacing-sm`: 8px
- `--spacing-md`: 16px
- `--spacing-lg`: 24px
- `--spacing-xl`: 32px

**Shape:**
- `--md-sys-shape-corner-small`: 8px
- `--md-sys-shape-corner-medium`: 16px
- `--md-sys-shape-corner-full`: 9999px (capsule)

## Project Structure

```
architecture-tools/
├── src/
│   ├── tools/           # Individual tool implementations
│   ├── components/      # Project-specific components (if needed)
│   └── styles/          # Project-specific styles
├── public/              # Static assets
├── index.html           # Main entry point
├── CLAUDE.md            # AI assistant instructions
└── agents.md            # Pointer for non-Claude AI tools
```

## Development

```bash
# Start local development server
npx serve .

# Or with Vite (if added)
npm run dev
```

## Code Style

- Use ES modules
- Prefer web components (LitElement) for reusable UI
- Keep tools self-contained and focused
- Document each tool's purpose and usage

## Communication Preferences

**Be concise.** Prefer brief, direct communication over verbose documentation.

- Do NOT create markdown documentation files unless explicitly requested
- Do NOT write long summaries after completing tasks
- Focus on action over commentary

## CSS Quality Standards

- NEVER use `!important`
- Always use design tokens, never hardcode values
- Follow the design system's token precedence
