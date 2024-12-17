import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

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
