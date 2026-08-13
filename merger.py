from config import client, MODEL
from prompts import MERGE_PROMPT


def merge_summaries(summaries):
    """
    Merge multiple summaries into one.
    """

    combined = "\n\n".join(summaries)

    prompt = MERGE_PROMPT.format(text=combined)

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text