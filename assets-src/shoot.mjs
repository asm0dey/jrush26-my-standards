// Capture a GitHub PR header as a deck asset. Dark to match the deck.
import { chromium } from 'playwright-chromium'

const [url, out, clip] = process.argv.slice(2)
const browser = await chromium.launch()
const page = await browser.newPage({
  viewport: { width: 1400, height: 900 },
  colorScheme: 'dark',
  deviceScaleFactor: 2,
})
await page.goto(url, { waitUntil: 'networkidle' })
await page.addStyleTag({ content: '.js-notification-shelf, .flash, header.AppHeader { display:none !important }' })
// clip is "x,y,w,h" in CSS pixels; GitHub's React layout has no stable selector
const box = clip ? Object.fromEntries(
  ['x','y','width','height'].map((k, i) => [k, Number(clip.split(',')[i])])) : null
await page.screenshot({ path: out, ...(box ? { clip: box } : { fullPage: false }) })
await browser.close()
console.log('wrote', out)
