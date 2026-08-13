import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key Loaded:", api_key is not None)

client = genai.Client(api_key=api_key)

MODEL = "models/gemini-3.5-flash"

