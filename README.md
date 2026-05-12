# fuzzy-switcher

A keyboard-driven window switcher for macOS. Lists all open windows and focuses the one you pick — faster than Alt-Tab when you have a lot of windows open.

## Why

macOS's built-in window switcher is application-level, not window-level. If you have six browser windows, six terminal sessions, and a handful of editor windows open, Alt-Tab is useless. This tool gives you a flat, enumerable list of every open window so you can get to the right one without mousing around.

## Status

Working: window enumeration and focus via pyobjc bindings to the macOS Accessibility API.
In progress: fuzzy search ranking (`src/fuzzy.py`) — currently you select by index.

```
0 Terminal — ~/projects/fuzzy-switcher
1 Firefox — GitHub
2 PyCharm — main.py
3 Terminal — ~/
Choose a window by index: 2
```

## Requirements

- macOS (uses the Accessibility API — won't run on Linux/Windows)
- Python 3.11+
- Accessibility permissions granted to Terminal (System Settings → Privacy & Security → Accessibility)

## Install

```bash
git clone https://github.com/ciguarin/fuzzy-switcher
cd fuzzy-switcher
pip install -e .
```

## Run

```bash
python main.py
```

## Roadmap

- [ ] Fuzzy search ranking (fzf-style substring scoring)
- [ ] Hotkey activation (global shortcut to open the switcher)
- [ ] Recency-based ranking (surfaces recently used windows first)
