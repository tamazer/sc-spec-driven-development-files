# Validation: Hello Hono

## Definition of done

All of the following are true before this branch merges.

### 1. Typecheck

```
npm run typecheck
```

Exits 0. `tsconfig.json` still has `"strict": true`.

### 2. Tests are wired, and none are required

```
npm test
```

Exits 0. Vitest is installed. No test files are required. The script includes `--passWithNoTests`.

### 3. Dev server

```
npm run dev
```

Starts without an error and listens on port 3000 (or the logged `PORT`).

### 4. The route is the minimal home page

```
curl -s -D - http://localhost:3000
```

Status is `200`. The body is HTML from `Home` inside `Layout`, and contains:

- `<header>`, `<main>`, and `<footer>`
- `<h1>` whose text is `AgentClinic`
- `<p>` whose text is exactly `AgentClinic is open for business`
- a stylesheet link to `/static/style.css`

A body that is only the plain sentence, with no `<h1>`, does not pass. No other page route is required.

### 5. The stylesheet is served

```
curl -s -D - http://localhost:3000/static/style.css
```

Status is `200`. The body is the contents of `static/style.css`.

### 6. Header, main, and footer are separate files

These files exist, and each exports only its own component:

- `src/components/Header.tsx`
- `src/components/Main.tsx`
- `src/components/Footer.tsx`

`src/components/Layout.tsx` imports all three. It does not define `Header`, `Main`, or `Footer`.

### 7. Hono is pinned

`package.json` lists `hono` and `@hono/node-server` with exact versions: no `^` and no `~`.

### 8. Tone

Page copy is `AgentClinic` and `AgentClinic is open for business`. The header repeats `AgentClinic`. The footer is a copyright line with the year and `AgentClinic`. No extra tagline, joke, or marketing sentence.

## Not required

- A navigation list
- A database
- A test that requests `/`
- A browser check (`curl` is enough)
- CI
