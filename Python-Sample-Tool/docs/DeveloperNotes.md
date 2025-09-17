# Developer Notes – Daily Inspiration CLI
```python
import requests
from datetime import datetime
import random
```
- **requests** → allows HTTP requests to APIs.
- **datetime** → used to display the current date/time.
- **random** → selects a random fallback quote if the API fails.


---


## 2. Fallback Quotes
```python
FALLBACK_QUOTES = [
"...",
"...",
]
```
This is a list of predefined quotes. It ensures the program always works even if the API is unreachable (e.g., network issue, API downtime).


---


## 3. Quote Fetching Function
```python
def get_quote():
...
```
- Tries to call the ZenQuotes API (`https://zenquotes.io/api/random`).
- If successful → parses JSON and formats the quote with author.
- If unsuccessful → falls back to a random choice from `FALLBACK_QUOTES`.


Error handling (`try/except`) ensures the script never crashes on a bad API response.


---


## 4. Main Program
```python
if __name__ == "__main__":
```
This block only runs when the script is executed directly.


It:
1. Prints a decorative header (`"="*50`).
2. Shows the current date/time using `datetime.now().strftime(...)`.
3. Calls `get_quote()` and prints the result.
4. Closes with another line of `=` for symmetry.


---


## 5. Example Run
```
==================================================
💡 Daily Inspiration CLI 💡
Date: 2025-09-06 17:23:30
==================================================
“The best way to get started is to quit talking and begin doing.” — Walt Disney
==================================================
```


---


## 6. Why This Matters
- Shows understanding of **APIs, JSON parsing, error handling, and fallback logic**.
- Demonstrates ability to **document code for both developers and end-users**.
- Serves as a reusable **portfolio project** to highlight technical writing and engineering skill.
```