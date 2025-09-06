# Daily Inspiration CLI – User Guide


## Overview
The Daily Inspiration CLI is a lightweight Python tool that fetches and displays a random inspirational quote.
It demonstrates how to integrate with a public API (ZenQuotes) and gracefully fall back to offline data if needed.


---


## Installation
1. Clone this repository:
```bash
git clone https://github.com/timboblackburn/Technical-Writing.git
cd Technical-Writing/Python-Sample-Tool
```


2. Install dependencies:
```bash
pip install -r requirements.txt
```


---


## Usage
Run the script with:
```bash
python inspire.py
```


Example output:
```
==================================================
💡 Daily Inspiration CLI 💡
Date: 2025-09-06 17:23:30
==================================================
“A bird does not sing because it has an answer. It sings because it has a song.” — Chinese Proverb
==================================================
```


---


## Customization
- Add or replace quotes in the `FALLBACK_QUOTES` list inside `inspire.py`.
- Swap the ZenQuotes API for another data source (facts, jokes, news).
```
