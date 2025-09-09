# Inspirational CLI Tutorial

Welcome! This notebook will walk you through building and understanding the **Daily Inspiration CLI** project step by step.  

By the end, you will understand:
1. How to **import Python modules**.
2. How to **define fallback quotes** using lists.
3. How to **fetch live data from an API**.
4. How to **gracefully handle errors**.
5. How to **run the full CLI tool**.

We’ll use beginner-friendly explanations so even if you’re new to Python, you’ll understand what’s happening.

## Step 1: Importing Required Modules  

We need to load some tools (called *modules* or *libraries*) that extend Python’s abilities:  

- `requests`: lets us fetch live data from APIs on the internet.  
- `datetime`: lets us print the current date/time.  
- `random`: lets us randomly pick a fallback quote if the API fails.  



```python
import requests
from datetime import datetime
import random

```

## Step 2: Define Fallback Quotes  

Sometimes the API won’t respond (bad internet, server down, etc.).  
To make sure our program *always* shows something, we’ll prepare a **list of backup quotes**.  



```python
FALLBACK_QUOTES = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs"
]

```

## Step 3: Fetch Quotes from the API  

We’ll use the **ZenQuotes API** to fetch real inspirational quotes.  

This code:  
1. Sends a request to `https://zenquotes.io/api/random`.  
2. If the request succeeds, it grabs the quote text + author.  
3. If the request fails, it picks one from our `FALLBACK_QUOTES`.  



```python
def get_quote():
    """Fetch a random inspirational quote from ZenQuotes API or fallback list."""
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"“{data[0]['q']}” – {data[0]['a']}"
    except Exception:
        return random.choice(FALLBACK_QUOTES)

```

## Step 4: Run the CLI  

Now let’s bring it all together.  
We’ll print a **header**, today’s **date/time**, and an inspirational quote.  



```python
print("="*50)
print("💡 Daily Inspiration CLI 💡")
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("="*50)
print(get_quote())
print("="*50)

```
