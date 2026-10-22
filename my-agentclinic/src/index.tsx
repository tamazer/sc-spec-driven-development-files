import { serve } from "@hono/node-server";
import { serveStatic } from "@hono/node-server/serve-static";
import { Hono } from "hono";
import { Home } from "./pages/Home.js";

const app = new Hono();

app.use("/static/*", serveStatic({ root: "./" }));

app.get("/", (c) => {
  return c.html(<Home />);
});

const port = process.env.PORT ? Number(process.env.PORT) : 3000;

serve({ fetch: app.fetch, port }, (info) => {
  console.log(`Server running at http://localhost:${info.port}`);
});
