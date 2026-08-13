def analyze(text):
    """
    Decide whether the text is short or long.
    """

    word_count = len(text.split())

    print(f"Word Count: {word_count}")

    if word_count < 500:
        return "short"

    return "long"