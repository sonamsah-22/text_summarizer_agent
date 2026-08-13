from chunker import split_text

text = input("Enter text:\n")

chunks = split_text(text, chunk_size=10)

print(f"\nTotal Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:")
    print(chunk)
    print("-" * 40)