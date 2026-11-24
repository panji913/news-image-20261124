# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/panji913/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/panji913/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A single 1024×1024 poster summing up the world news of Tuesday 24 November 2026 in six verified stories: the Cikande factory-fire toll, Ukraine sinking a Russian warship off Libya, Nvidia reinstating Jensen Huang, the ~700,000 Russian war dead, the EU's 22nd sanctions package, and the US blacklisting Megaspeed.

## The six stories

All six were first reported in the 24 November 2026 news cycle and checked against their sources on 24 Nov 2026:

1. **Indonesia** — Factory fire toll: 24 dead, ~30 missing (officials via AP / Xinhua).
2. **Ukraine · Libya** — Kyiv sinks Russian warship off Libya (AP).
3. **Tech** — Nvidia brings back Jensen Huang (Nvidia / Morningstar).
4. **Russia** — Russian war dead near 700,000 (Meduza / Mediazona).
5. **Europe** — EU proposes 22nd Russia sanctions package (European Commission).
6. **USA · China** — US blacklists firm in Nvidia spy case (US Bureau of Industry and Security).

## Build

The poster is drawn by `draw.py` (PIL only, no network, no clock, no randomness) and copied to the grader's output path by `main.ts`. Two runs produce byte-identical files: 118,593 bytes, 1024×1024, sha256 `8cf549617be4f8ef2452c29abd628582d0f460d0fc9711689368d43d5143133b`.

## Files

- `draw.py` — draws `entry.png`.
- `entry.png` — the verified poster.
- `main.ts` — copies `entry.png` to `MAKEFUN_OUTPUT_DIR` (default `/output`).
- `out/` — local render output.

## Run it

```sh
python3 draw.py && mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=7q825rck&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
