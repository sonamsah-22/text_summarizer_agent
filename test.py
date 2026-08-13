from config import client

response = client.models.generate_content(
    model="models/gemini-3.5-flash-lite",
    contents="Explain AI agents in simple words."
)

print(response.text)