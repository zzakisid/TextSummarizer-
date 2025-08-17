from transformers import pipeline
import textwrap

# Initialize summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def chunk_text(text, chunk_size=750):
    # Split the text into chunks of roughly 750 words (which is ~1024 tokens)
    words = text.split()
    chunks = textwrap.wrap(" ".join(words), width=chunk_size)
    return chunks

def summarize_large_text(text):
    chunks = chunk_text(text)
    summaries = []

    # Summarize each chunk
    for chunk in chunks:
        summary = summarizer(chunk, max_length=200, min_length=50, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    # Join all summaries together
    full_summary = " ".join(summaries)
    return full_summary
