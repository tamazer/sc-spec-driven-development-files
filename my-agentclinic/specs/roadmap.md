# Roadmap

Phases are intentionally small — each one is a shippable slice, independently reviewable and demoable.

Strategy: **Hello world first** (working server + layout), then Susan's domain (agents → ailments → therapies → booking), then Mary's dashboard and Steve's polish.

Each phase is validated with `npm test` (Vitest).

The web UI is mobile-first, as in `specs/tech-stack.md`. Base styles fit a narrow screen. `min-width` media queries add room on wider screens. Every page includes a viewport meta tag. Brand colors are orange and black, held in custom properties as in `specs/tech-stack.md`.

---

## Phase 1 — Hello Hono ✅
- Install and configure Hono with `tsx` dev server
- Single `/` route returning "AgentClinic is open for business"
- Confirm TypeScript types work end-to-end

## Phase 2 — Layout, agents, and ailments
- Shared layout (header, nav, main, footer)
- Basic CSS (custom properties, typography)
- All routes render inside the shared layout
- Persistence layer + first `agents` table/migration
- Seed a handful of fictional agents
- `/agents` page listing all agents
- `/agents/:id` profile page
- Name, model type, status, presenting complaints
- `ailments` table + seed data (e.g. context-window claustrophobia, prompt fatigue)
- `/ailments` list page
- Link agents to one or more ailments

## Phase 3 — Therapies catalog
- `therapies` table + seed data
- `/therapies` list page
- Map ailments → recommended therapies

## Phase 4 — Appointment booking
- `appointments` table (agent, therapist, datetime, status)
- Book from an agent's detail page
- Validation + confirmation

## Phase 5 — Staff dashboard
- `/dashboard` with summary counts (agents, open appointments, ailments in flight)
- Simple tables for staff — Mary's dashboard becomes real

## Phase 6 — Polish
- Audit every page against the mobile-first rule above
- Semantic HTML / basic accessibility

## Phase 7 — Hardening
- 404/500 pages
- Input sanitization on forms
- Basic logging middleware

---

Later (not scheduled): auth, email notifications, therapist profiles, richer reporting.
