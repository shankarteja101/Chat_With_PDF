import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def query_and_retrieve(query, index):
    """Queries the vector database and retrieves relevant chunks.

    Args:
        query (str): User's natural language query.
        index (faiss.IndexFlatL2): FAISS index.

    Returns:
        list: List of retrieved chunks.
    """

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query])[0]
    distances, indices = index.search(query_embedding.reshape(1, -1), k=5)

    retrieved_chunks = [chunks[i] for i in indices[0]]
    return retrieved_chunks

def generate_response(query, retrieved_chunks):
    """Generates a response using an LLM.

    Args:
        query (str): User's natural language query.
        retrieved_chunks (list): List of retrieved chunks.

    Returns:
        str: Generated response.
    """

    # Load a pre-trained seq2seq model (e.g., T5)
    model_name = "t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Create a prompt combining the query and retrieved chunks
    prompt = f"Question: {query}\n\nContext: {''.join(retrieved_chunks)}\n\nAnswer:"

    # Generate the response
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids)
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return generated_text

# Example usage:
query = "What is the unemployment rate for engineering graduates?"
retrieved_chunks = query_and_retrieve(query, index)
response = generate_response(query, retrieved_chunks)

print(response)
