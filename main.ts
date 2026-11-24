// news-image-20261124 — poster for Tuesday 24 November 2026.
// Entry for @panji913. The poster (entry.png, rendered in-session by
// draw.py with PIL) sums up the day in six verified stories: the
// Cikande factory-fire toll, Ukraine's strike on a Russian warship
// off Libya, Nvidia reinstating Jensen Huang, the ~700,000 Russian
// war dead estimated from leaked Rosstat data, the EU's 22nd Russia
// sanctions package, and the US blacklisting Megaspeed.
//
// This program places that image at the grader's output path. It is
// deterministic: identical bytes in, identical bytes out, no network.
//
// Run locally:  python3 draw.py && mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, 'entry.png');
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

if (!existsSync(src)) {
  throw new Error(`entry.png not found next to main.ts (${here})`);
}
const size = statSync(src).size;
if (size > 1048576) {
  throw new Error(`entry.png is ${size} bytes, over the 1 MiB cap`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(src, join(outDir, 'entry.png'));
console.log(`copied entry.png (${size} bytes) to ${outDir}`);
