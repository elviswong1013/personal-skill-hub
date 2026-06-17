# Color Scheme & PPT Specifications

Visual styling for HTML and PPTX output. Apply these values when generating presentation files.

## Color Palette

| Role | Hex | R | G | B | Usage |
|---|---|---|---|---|---|
| Dark background | `#0B1D2E` | 11 | 29 | 46 | Full-slide backgrounds, dark sections |
| Medium background | `#122D44` | 18 | 45 | 68 | Card backgrounds, alternate rows |
| Teal accent | `#00B4A0` | 0 | 180 | 160 | Headers, badges, table headers, decorative lines |
| White text | `#FFFFFF` | 255 | 255 | 255 | Body text on dark backgrounds |
| Gold accent | `#F0C040` | 240 | 192 | 64 | Highlights, star ratings, emphasis |
| Orange accent | `#FF8C42` | 255 | 140 | 66 | Warnings, safety notices, alerts |

## PPT Layout Specs

- **Slide dimensions**: 16:9 widescreen (13.333" × 7.5")
- **Title slide**: Large centered title + teal decorative lines
- **Content pages**: Teal bar at top (0.3" height) + transparent page number at bottom
- **Tables**: Teal header row + alternating row colors (dark/medium)
- **Day detail pages**: Teal rounded badge for day number + bullet highlights on left + tip card on right
- **Feature cards**: Grid layout with medium background + teal accent border

## HTML Specs

- **Theme**: Dark Nordic (`#0B1D2E` base + `#00B4A0` teal + white text)
- **Slides**: Each section uses `min-height: 100vh` for full-screen effect
- **Layout**: CSS Grid for feature cards and packing categories
- **Tables**: Teal headers + alternating row colors + hover highlight
- **Responsive breakpoints**: 1024px (tablet) and 640px (mobile)
- **Print stylesheet**: `@media print` with white background, black text, page-break per slide
- **Micro-interactions**: Card hover lift (`transform: translateY(-2px)`) + glowing teal border

## Dependencies

For PPTX generation, use the project's available PPT generation library. The structure adapts to whatever library is available — the key outputs are slides, tables, cards, and badges following the color scheme above.
