# Tech Stack

AgentClinic is a server-side TypeScript application. All rendering happens on the server; the browser receives plain HTML that works on narrow and wide screens.

## Core

| Layer | Choice | Rationale |
|---|---|---|
| Language | TypeScript | Type safety end-to-end; satisfies Mary's requirement |
| Runtime | Node.js | Stable, well-supported, vast ecosystem |
| Server framework | **Hono** | Lightweight, TypeScript-first, fast, excellent DX; routes and middleware feel natural |
| Templating | Hono JSX (server-side) | JSX without React overhead; components are just functions |
| CSS | Plain CSS + CSS custom properties | No build step required; mobile-first layout in orange and black so Steve's page works on a phone and a desktop |

## Recommended: Hono

[Hono](https://hono.dev) is chosen over Express/Fastify because:

- First-class TypeScript with zero config
- Built-in JSX renderer for server-side HTML
- Middleware model is simple and composable
- Runs on Node, Deno, Bun, and edge runtimes without changes

## Data

- **SQLite** (via `better-sqlite3`) for local development and early production — simple, embedded, no infrastructure
- Migrations via plain SQL files; no ORM to start

## CSS

The UI is mobile-first. Base styles target a narrow screen. `min-width` media queries add space on wider screens. Custom properties hold color, type, and spacing so those values stay shared across breakpoints. One stylesheet, no CSS framework, no build step. Every document includes `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.

Brand colors are orange and black. The stylesheet defines `--color-brand-orange` (`#e85d04`) and `--color-brand-black` (`#111111`). The header is black, with an orange wordmark and accent. Body text uses the black. The page background stays white so the copy stays readable.

## Testing

Feature validation is a Vitest suite. A phase is validated by running that suite.

- **Vitest** — fast, TypeScript-native, compatible with the rest of the stack
- `npm test` runs `vitest run --passWithNoTests`, so a suite with no test files still exits 0

## Tooling

- `tsx` for development (run TypeScript directly, no build step needed)
- `tsc` for production builds
- `prettier` for formatting
- `npm test` for validation (`vitest run --passWithNoTests`)

## What We Are Not Using

- No React, Vue, or Svelte — server-side rendering keeps the stack simple
- No ORM — SQL is sufficient at this scale
- No Docker — not yet; that's a later phase concern
