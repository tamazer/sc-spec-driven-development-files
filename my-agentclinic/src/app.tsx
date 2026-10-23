import { serveStatic } from "@hono/node-server/serve-static";
import { Hono } from "hono";
import { Home } from "./pages/Home.js";

export function createApp() {
  const app = new Hono();

  app.use("/static/*", serveStatic({ root: "./" }));

  app.get("/", (c) => {
    return c.html(<Home />);
  });

  return app;
}
