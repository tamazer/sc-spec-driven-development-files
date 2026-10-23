import { serve } from "@hono/node-server";
import { createApp } from "./app.js";

const app = createApp();

const port = process.env.PORT ? Number(process.env.PORT) : 3000;

serve({ fetch: app.fetch, port }, (info) => {
  console.log(`Server running at http://localhost:${info.port}`);
});
