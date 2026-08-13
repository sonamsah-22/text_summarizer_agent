SUMMARY_PROMPT = """
You are an expert text summarizer.

Summarize the following text into 5 concise bullet points.

Text:
{text}
"""

MERGE_PROMPT = """
You are an expert editor.

You are given summaries of different parts of one document.

Merge them into one final summary.

Rules:
- Remove duplicate information.
- Keep all important points.
- Produce exactly 5 bullet points.
- Make it flow naturally.

Summaries:
{text}
"""