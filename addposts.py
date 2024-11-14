tokens = [
    "92f221ed7efb6ecd0354d903c72b4af95221f3dd",
    "1a4ada956780a73639828b6a030c79ff6efbb5ad",
    "ce7ec886eead7ea3ff4582e084efc0c8baf2f112",
    "e50ad37c17fc6973bd41a64e3a243c774f145dfb",
]

import requests
import random

# URL for creating posts
url = "http://127.0.0.1:8000/posts/"

# Make 10 post requests
for i in range(20, 30):
    # Randomly select a token
    token = random.choice(tokens)

    # Set up headers with token
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}

    # Post data
    data = {"text": f"Post {i}"}

    # Send POST request
    response = requests.post(url, json=data, headers=headers)

    # Print response status
    print(f"Request {i+1} status: {response.status_code}")
    if response.status_code != 201:
        print(f"Error: {response.text}")
