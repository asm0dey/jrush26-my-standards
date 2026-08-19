import { chromium } from 'playwright-chromium'
import { readdirSync, readFileSync, statSync } from 'node:fs'
import { join, relative } from 'node:path'
// Contact sheet of every spec-kit artifact: the mass is the message, not the words.
const ROOT = '/home/finkel/work_self/femtocli/specs/001-codegen-parser'
const walk = d => readdirSync(d).flatMap(e => {
  const f = join(d, e)
  return statSync(f).isDirectory() ? walk(f) : [f]
}).sort()
const docs = walk(ROOT).map(f => ({ name: relative(ROOT, f), text: readFileSync(f, 'utf8').slice(0, 6000) }))
const page = d => `<div class="pg"><div class="hd">${d.name}</div><div class="tx">${
  d.text.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}</div></div>`
const html = `<style>
  *{box-sizing:border-box}
  body{margin:0;background:#0d0d0d;font-family:'JetBrains Mono',ui-monospace,monospace}
  .sheet{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;padding:24px;width:2400px}
  .pg{background:#f4f2ee;color:#3a3a38;height:300px;overflow:hidden;padding:8px;border-radius:2px;
      box-shadow:0 2px 10px rgba(0,0,0,.5)}
  .hd{font-size:5px;font-weight:700;color:#111;margin-bottom:4px;letter-spacing:.2px}
  .tx{font-size:2.6px;line-height:1.5;white-space:pre-wrap;word-break:break-word}
</style><div class="sheet">${docs.map(page).join('')}</div>`
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 2400, height: 1400 }, deviceScaleFactor: 1 })
await p.setContent(html); await p.waitForTimeout(400)
await p.locator('.sheet').screenshot({ path: process.argv[2] || 'public/spec-kit-sheet.png' })
await b.close(); console.log('wrote public/spec-kit-sheet.png')
