import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { createApp } from "../src/app.js";

const app = createApp();

describe("GET /", () => {
  it("returns the home page inside the layout", async () => {
    const response = await app.request("/");
    const html = await response.text();

    expect(response.status).toBe(200);
    expect(response.headers.get("content-type")).toContain("text/html");
    expect(html).toContain("<header>");
    expect(html).toContain("<main>");
    expect(html).toContain("<footer>");
    expect(html).toContain("<h1>AgentClinic</h1>");
    expect(html).toContain("<p>AgentClinic is open for business</p>");
    expect(html).toContain('href="/static/style.css"');
    expect(html).toContain(
      '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>',
    );
    expect(html).not.toBe("AgentClinic is open for business");
  });

  it("keeps the page copy to the name, the tagline, and the copyright line", async () => {
    const response = await app.request("/");
    const html = await response.text();
    const year = new Date().getFullYear();

    expect(html).toContain('<a href="/">AgentClinic</a>');
    expect(html).toContain(`<p>© ${year} AgentClinic</p>`);
  });
});

describe("GET /static/style.css", () => {
  it("returns the stylesheet file", async () => {
    const response = await app.request("/static/style.css");
    const css = await response.text();
    const file = readFileSync("static/style.css", "utf8");

    expect(response.status).toBe(200);
    expect(response.headers.get("content-type")).toContain("text/css");
    expect(css).toBe(file);
    expect(css).toContain("--color-text");
    expect(css).toMatch(/@media\s*\(\s*min-width:/);
  });
});
