# from analyzer import analyze
# from chunker import split_text
# from summarizer import summarize
# from merger import merge_summaries


# def run_agent(text):
#     """
#     Main AI Agent
#     """

#     print("\n🔍 Analyzing document...")

#     decision = analyze(text)

#     print(f"Decision: {decision}")

#     if decision == "short":

#         print("📝 Direct summarization...")

#         return summarize(text)

#     print("📄 Long document detected.")

#     chunks = split_text(text)

#     print(f"Created {len(chunks)} chunks.\n")

#     summaries = []

#     for i, chunk in enumerate(chunks, start=1):

#         print(f"Summarizing Chunk {i}...")

#         summaries.append(summarize(chunk))

#     print("\n🔄 Merging summaries...")

#     final_summary = merge_summaries(summaries)

#     return final_summary


# if __name__ == "__main__":

#     text = input("Paste your text:\n\n")

#     summary = run_agent(text)

#     print("\n==============================")
#     print("FINAL SUMMARY")
#     print("==============================\n")

#     print(summary)

import time

from analyzer import analyze
from chunker import split_text
from summarizer import summarize
from merger import merge_summaries


def typewriter(text, delay=0.05):
    """
    Prints text word-by-word while preserving bullet points and new lines.
    """

    # Split the response into lines
    lines = text.split("\n")

    for line in lines:

        # Empty line
        if not line.strip():
            print()
            continue

        # Print each word in the current line
        for word in line.split():
            print(word, end=" ", flush=True)
            time.sleep(delay)

        # Move to next line after finishing this bullet
        print()

        # Small pause before the next bullet
        time.sleep(0.3)


def run_agent(text):
    """
    Main AI Agent
    """

    print("\n🔍 Analyzing document...\n")

    decision = analyze(text)

    print(f"📊 Decision: {decision.upper()}\n")

    # Short document
    if decision == "short":

        print("📝 Generating summary...\n")

        summary = summarize(text)

        print("========== FINAL SUMMARY ==========\n")

        typewriter(summary)

        return

    # Long document
    print("📄 Long document detected.")

    chunks = split_text(text)

    print(f"📦 Created {len(chunks)} chunks.\n")

    summaries = []

    for i, chunk in enumerate(chunks, start=1):

        print(f"📝 Summarizing Chunk {i}/{len(chunks)}...")

        chunk_summary = summarize(chunk)

        summaries.append(chunk_summary)

        print("✅ Done\n")

    print("🔄 Merging summaries...\n")

    final_summary = merge_summaries(summaries)

    print("========== FINAL SUMMARY ==========\n")

    typewriter(final_summary)


if __name__ == "__main__":

    print("=" * 60)
    print("🤖 AI TEXT SUMMARIZER AGENT")
    print("=" * 60)

    text = input("\nPaste your text:\n\n")

    run_agent(text)