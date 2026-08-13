from config import client, MODEL
from prompts import SUMMARY_PROMPT


def summarize(text):
    prompt = SUMMARY_PROMPT.format(text=text)

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text