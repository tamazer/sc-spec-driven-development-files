# Roadmap

Phases are intentionally small — each one is a shippable slice, independently reviewable and demoable.

Strategy: **Hello world first** (working server + layout), then Susan's domain (agents → ailments → therapies → booking), then Mary's dashboard and Steve's polish.

---

## Phase 1 — Hello Hono ✅
- Install and configure Hono with `tsx` dev server
- Single `/` route returning "AgentClinic is open for business"
- Confirm TypeScript types work end-to-end

## Phase 2 — Base layout
- Shared layout (header, nav, main, footer)
- Basic CSS (custom properties, typography)
- All routes render inside the shared layout

## Phase 3 — Agent list
- Persistence layer + first `agents` table/migration
- Seed a handful of fictional agents
- `/agents` page listing all agents

## Phase 4 — Agent detail
- `/agents/:id` profile page
- Name, model type, status, presenting complaints

## Phase 5 — Ailments catalog
- `ailments` table + seed data (e.g. context-window claustrophobia, prompt fatigue)
- `/ailments` list page
- Link agents to one or more ailments

## Phase 6 — Therapies catalog
- `therapies` table + seed data
- `/therapies` list page
- Map ailments → recommended therapies

## Phase 7 — Appointment booking
- `appointments` table (agent, therapist, datetime, status)
- Book from an agent's detail page
- Validation + confirmation

## Phase 8 — Staff dashboard
- `/dashboard` with summary counts (agents, open appointments, ailments in flight)
- Simple tables for staff — Mary's dashboard becomes real

## Phase 9 — Polish
- Responsive layout for modern browsers (Steve)
- Semantic HTML / basic accessibility

## Phase 10 — Hardening
- 404/500 pages
- Input sanitization on forms
- Basic logging middleware

---

Later (not scheduled): auth, email notifications, therapist profiles, richer reporting.
