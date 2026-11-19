// Copies the built static blog into dist/ so hosts that run "npm run build" and publish "dist" serve it.
import fs from "fs";
fs.rmSync("dist", { recursive: true, force: true });
fs.mkdirSync("dist");
const skip = new Set(["dist", "node_modules", ".git", "build.py", "build-dist.mjs", "package.json", "package-lock.json"]);
for (const f of fs.readdirSync(".")) if (!skip.has(f) && !f.startsWith(".")) fs.cpSync(f, "dist/" + f, { recursive: true });
console.log("copied blog to dist/");
