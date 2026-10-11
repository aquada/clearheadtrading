import { readFileSync } from 'node:fs';

const MAX_CHARS = 900;
const BANNED = [
  /\b403\b/, /WebSearch/i, /WebFetch/i, /secondary[- ]source/i, /primary[- ]source/i,
  /re-?verif/i, /re-?check/i, /automated (fetch|access)/i, /\bblocked\b/i,
  /\bpending\b/i, /\bunconfirmed\b/i, /\btreat (as|it|them)\b/i, /\bdo not\b/i,
  /\bdon'?t\b/i, /\bactive:\s*(true|false)/i, /\bnot (been )?confirmed\b/i,
];

const files = ['static/data/propfirms.json', 'static/data/brokers.json'];
let failures = 0;

for (const file of files) {
  const data = JSON.parse(readFileSync(file, 'utf8'));
  const list = data.firms ?? data.brokers ?? [];
  for (const item of list) {
    const notes = item.notes ?? '';
    const where = `${file} :: ${item.name}`;
    if (notes.length > MAX_CHARS) {
      console.error(`${where}: notes ${notes.length} chars (max ${MAX_CHARS})`);
      failures++;
    }
    for (const pattern of BANNED) {
      const m = notes.match(pattern);
      if (m) {
        console.error(`${where}: process wording "${m[0]}" - rewrite as a visitor-facing fact`);
        failures++;
      }
    }
  }
}

if (failures) {
  console.error(`\n${failures} problem(s). See the note rules in scripts/check-compare-notes.mjs.`);
  process.exit(1);
}
console.log('compare notes OK');
