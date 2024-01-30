import requests
import json

# Read the contents of the "keywords.txt" file
with open("keywords.txt", "r") as file:
    keywords = file.read().strip()

# Create a JSON payload
payload = {
    "keywords": keywords
}

# Send the JSON payload to the server
url = "http://www.example.com"
response = requests.post(url, json=payload)

# Print the response from the server
print(response.text)
