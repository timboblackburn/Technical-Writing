import requests
from datetime import datetime
import random

FALLBACK_QUOTES = [
    "“The best way to get started is to quit talking and begin doing.” — Walt Disney",
    "“Don’t let yesterday take up too much of today.” — Will Rogers",
    "“It’s not whether you get knocked down, it’s whether you get up.” — Vince Lombardi",
    "“If you are working on something exciting, it will keep you motivated.” — Steve Jobs",
]

def get_quote():
    """Fetch a random inspirational quote from ZenQuotes API or fallback list."""
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"“{data[0]['q']}” — {data[0]['a']}"
    except Exception:
        return random.choice(FALLBACK_QUOTES)

if __name__ == "__main__":
    print("="*50)
    print("💡 Inspirational Quotes 💡")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)
    print(get_quote())
    print("="*50)