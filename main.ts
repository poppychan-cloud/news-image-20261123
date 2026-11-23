// news-image-20261123 entry (Node 22, standard library only):
// the image is the entry.png beside this file, drawn by draw.py
// (Python PIL, code-rendered text so nothing is garbled),
// and this program copies it to /output/entry.png.
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
