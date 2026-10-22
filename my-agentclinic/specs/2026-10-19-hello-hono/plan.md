# Plan: Hello Hono

## Group 1 — Dependencies

1. Install `hono` and `@hono/node-server`. Remove any `^` or `~` so both versions are pinned.
2. Install `tsx` and `vitest` as dev dependencies.
3. Install `@types/node` as a dev dependency so `tsc` understands Node.

## Group 2 — TypeScript config

4. Keep `"strict": true` in `tsconfig.json`.
5. Set `"jsx": "react-jsx"` and `"jsxImportSource": "hono/jsx"`.
6. Switch `module` and `moduleResolution` to settings that typecheck Hono's ESM (`NodeNext` or equivalent), and set `"type": "module"` in `package.json`.
7. Keep `include` pointed at `src`.

## Group 3 — Application entry

8. Replace `src/index.ts` with `src/index.tsx`: a Hono app and `serve()` from `@hono/node-server` on port 3000 (or `PORT`).
9. Add `GET /` returning the plain text `AgentClinic is open for business`, so the server is proven before the page exists.

## Group 4 — Minimal home page

10. Create `src/pages/Home.tsx`. It renders the document shell: `<html>`, `<head>` (charset and `<title>AgentClinic</title>`), and `<body>`. No stylesheet link. Group 7 moves this shell onto the shared layout.
11. The body contains `<h1>AgentClinic</h1>` and `<p>AgentClinic is open for business</p>`.
12. Change `GET /` so it returns the rendered `<Home />` as HTML instead of the plain string.

## Group 5 — Scripts

13. Add `"dev": "tsx watch src/index.tsx"`.
14. Add `"typecheck": "tsc --noEmit"`.
15. Add `"test": "vitest run --passWithNoTests"`.
16. Leave `"build": "tsc"` in place.

## Group 6 — Verify

17. Run `npm run typecheck` and confirm exit 0.
18. Run `npm test` and confirm exit 0 with no test files present.
19. Run `npm run dev` and confirm `GET /` returns 200 HTML containing the heading and the tagline from `Home`, not the plain string alone.

## Group 7 — Layout

20. Create `src/components/Layout.tsx`. It owns the document shell: `<html>`, `<head>`, and `<body>`. The head has a charset, a viewport meta, `<title>AgentClinic</title>`, and a stylesheet link.
21. Create `Header`, `Main`, and `Footer` as three subcomponents, one component per file: `src/components/Header.tsx`, `src/components/Main.tsx`, and `src/components/Footer.tsx`. Do not declare them inside `Layout.tsx`. `Layout` imports all three. `Main` wraps the page content.
22. Create `static/style.css` with minimal base styles: custom properties, typography, and rules for `header`, `main`, and `footer`.
23. Link that file from the layout head as `/static/style.css`. In `src/index.tsx`, import `serveStatic` from `@hono/node-server/serve-static` and serve the `static/` directory at `/static/*`.
24. Change `Home` so it renders inside `<Layout>` and no longer owns the document shell. The heading and the tagline stay the same, and they render inside `<Main>`.

## Group 8 — Verify the layout

25. Run `npm run typecheck` and confirm exit 0.
26. Confirm `GET /` returns 200 HTML that contains `<header>`, `<main>`, `<footer>`, the heading, the tagline, and a link to `/static/style.css`.
27. Confirm `GET /static/style.css` returns 200 and the stylesheet body.
