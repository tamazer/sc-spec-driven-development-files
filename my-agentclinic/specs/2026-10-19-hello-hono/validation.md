# Validation: Hello Hono

## Definition of done

All of the following are true before this branch merges.

### 1. Typecheck

```
npm run typecheck
```

Exits 0. `tsconfig.json` still has `"strict": true`.

### 2. Vitest validates the phase

```
npm test
```

Exits 0. The script is `vitest run --passWithNoTests`. The suite imports `createApp` from `src/app.tsx` and calls `app.request`. It runs from the project root.

The home-page request expects status `200` and HTML that contains:

- `<header>`, `<main>`, and `<footer>`
- `<h1>` whose text is `AgentClinic`
- `<p>` whose text is exactly `AgentClinic is open for business`
- a stylesheet link to `/static/style.css`
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

A body that is only the plain sentence, with no `<h1>`, does not pass.

The stylesheet request expects status `200` and the contents of `static/style.css`. That file uses custom properties and at least one `min-width` media query.

### 3. Dev server

```
npm run dev
```

Starts without an error and listens on port 3000 (or the logged `PORT`). `src/index.tsx` is the only module that calls `serve()`.

### 4. Header, main, and footer are separate files

These files exist, and each exports only its own component:

- `src/components/Header.tsx`
- `src/components/Main.tsx`
- `src/components/Footer.tsx`

`src/components/Layout.tsx` imports all three. It does not define `Header`, `Main`, or `Footer`.

### 5. Hono is pinned

`package.json` lists `hono` and `@hono/node-server` with exact versions: no `^` and no `~`.

### 6. Responsive layout

`GET /` includes the viewport meta from section 2. `static/style.css` follows the mobile-first rule in `specs/tech-stack.md`: custom properties, base styles for a narrow screen, and a `min-width` media query.

### 7. Tone

Page copy is `AgentClinic` and `AgentClinic is open for business`. The header repeats `AgentClinic`. The footer is a copyright line with the year and `AgentClinic`. No extra tagline, joke, or marketing sentence.

## Not required

- A navigation list
- A database
- A browser check
- CI
