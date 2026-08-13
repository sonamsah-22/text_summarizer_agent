# AI Text Summarizer Agent

An AI-powered text summarization system built using **Python and Google Gemini API**. The system uses a multi-step agentic workflow to analyze, process, summarize, and consolidate text into a concise final summary.

## How It Works

```text
User Input
    |
    v
Analyzer
    |
    +---- Short Text ----> Summarizer
    |
    +---- Long Text -----> Chunker
                              |
                              v
                       Summarize Chunks
                              |
                              v
                       Merge Summaries
                              |
                              v
                       Final Summary
```

## Key Components

* **Analyzer:** Determines whether the input is short or requires chunking.
* **Chunker:** Divides long documents into smaller, manageable sections.
* **Summarizer:** Uses the Gemini API to generate summaries for the text or individual chunks.
* **Merger:** Combines multiple chunk summaries into a single coherent final summary.
* **Output Handler:** Displays the generated summary progressively for a better user experience.

## Technology Stack

**Python | Google Gemini API | google-genai | python-dotenv**

## Agentic Workflow

Unlike a basic summarization application that directly sends text to an LLM, this system follows a multi-step workflow:

```text
Analyze → Decide → Process → Summarize → Merge → Return
```

The workflow is implemented using custom Python logic without LangGraph or other agent frameworks.

## Current Status

Working prototype with support for short and long text summarization.

## Future Enhancements

* PDF and DOCX document support
* Web-based user interface
* Real-time Gemini streaming
* Multiple summary formats
* AI-based summary quality review
* Summary history and document management

## Author

**Sonam Sah**
Computer Engineering Student
JSPM's Jayawantrao Sawant College of Engineering, Pune
