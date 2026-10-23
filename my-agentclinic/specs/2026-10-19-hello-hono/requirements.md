# Requirements: Hello Hono

Phase 1 from `specs/roadmap.md`. Prove that Node runs TypeScript, Hono serves a response, and the dev loop works. Nothing more.

## Scope

### In scope

- Install and configure Hono on Node, with a `tsx watch` dev server on port 3000.
- A single `GET /` route. It may return plain text while the server is being proved. The merged result is the home page inside the shared layout below.
- A shared layout: header, main, and footer, plus a mobile-first stylesheet linked from the document head and served from `static/`.
- `Header`, `Main`, and `Footer` each live in their own file. They are not declared inside `Layout.tsx`.
- TypeScript stays strict, and `tsc --noEmit` is the typecheck.
- Vitest validates this phase. `npm test` runs `vitest run --passWithNoTests` and the suite asserts `GET /` and `GET /static/style.css`.

### Minimal home page

`src/pages/Home.tsx` is a Hono JSX component. `GET /` renders it as HTML. The finished response is that page, not the roadmap sentence on its own.

### Page

| Piece | Value | Notes |
|---|---|---|
| Document | HTML | Hono JSX, not a plain string |
| Heading | `AgentClinic` | Exactly this text inside `<h1>` |
| Tagline | `AgentClinic is open for business` | The roadmap sentence, in a `<p>` |
| Shell | `<html>`, `<head>`, `<body>` owned by `Layout` | Imports `Header`, `Main`, and `Footer` from their own files |
| Stylesheet | `/static/style.css` | Mobile-first: custom properties, narrow-screen base, a `min-width` query |
| Viewport | `width=device-width, initial-scale=1.0` | On the layout `<head>` |

A `<title>` of `AgentClinic` is part of that shell, along with a charset and the viewport meta. The body copy stays the heading and the tagline. The header text is `AgentClinic`. The footer text is a copyright line with the year and `AgentClinic`.

### Out of scope

- A navigation list (Phase 2 still names nav; this phase's header is the site name only)
- SQLite, migrations, or any other data (Phase 3)
- Any page route other than `GET /`. The stylesheet at `/static/style.css` is the exception.
- CI, logging, 404/500 pages
- Prettier setup

## Decisions

- **Pin Hono.** `hono` and `@hono/node-server` are recorded at the exact versions npm resolves, with no `^` or `~`. Later phases do not upgrade them silently. `tsx`, `vitest`, and `typescript` may keep a range, matching the existing TypeScript dependency.
- **`@hono/node-server` is in scope.** Hono's core package does not bind a Node port. The Node adapter is how this stack serves HTTP. It is not a new framework.
- **`tsx watch` on port 3000.** The dev script reloads on change. The listen port is 3000 unless `PORT` is set.
- **Strict TypeScript stays on.** `tsconfig.json` already has `"strict": true`. That does not get relaxed. Add the JSX and module settings Hono needs (`jsx`, `jsxImportSource`, and ESM-compatible `module` / `moduleResolution`, plus `"type": "module"`) so `tsc --noEmit` can see the imports.
- **Vitest validates the phase.** `specs/tech-stack.md` makes `npm test` the validation command. The script stays `vitest run --passWithNoTests`. The suite calls `createApp()` from `src/app.tsx` and uses `app.request`. That module does not call `serve()`, so a test does not bind a port. Tests run from the project root, where `serveStatic({ root: "./" })` finds `static/`.
- **The layout owns the document shell.** `Home` renders the heading and tagline. `Layout` owns `<html>`, `<head>`, and `<body>`. `Main` wraps the page content.
- **Header, main, and footer are one component per file.** `src/components/Header.tsx`, `src/components/Main.tsx`, and `src/components/Footer.tsx` each export that one component. `src/components/Layout.tsx` imports them and does not define them.
- **The stylesheet is a static file.** `static/style.css` is linked from the head and served at `/static/style.css`. It follows `specs/tech-stack.md`: custom properties, compact base styles, and at least one `min-width` media query. No framework CSS.
- **The viewport meta is required.** `Layout` includes `<meta name="viewport" content="width=device-width, initial-scale=1.0">`. Responsive layout is part of this phase.
- **The home page replaces the plain string.** Group 3 may return `AgentClinic is open for business` as text. Group 4 switches `GET /` to `<Home />`. Definition of done is the HTML page inside the layout.
- **Tagline is the roadmap sentence.** The heading satisfies the HTML choice; the paragraph is exactly `AgentClinic is open for business`. Layout chrome may repeat the site name. No extra clinic copy.

## Context

- `specs/mission.md`: this is a teaching project. The first page a developer sees after clone-and-run should be obvious and small.
- `specs/tech-stack.md`: TypeScript, Node, Hono, Hono JSX, `tsx`, `tsc`, plain CSS, and Vitest for validation. SQLite is chosen for the product, and it is not used in this phase.
- **Mary** — strict TypeScript and a clean `tsc --noEmit`.
- **Susan** — agents, ailments, therapies, and booking wait for later phases.
- **Steve** — the page is readable on a narrow screen and a wide one. Mobile-first CSS starts in this phase. Phase 9 audits later pages.
- **Tone** — dry. Page copy is `AgentClinic` and `AgentClinic is open for business`. The header repeats the name. The footer is a copyright line.
- **Existing code** — `src/index.tsx` serves `Home` as a document shell with no stylesheet. Replace that shell with the layout; do not add a second app.
