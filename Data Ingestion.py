import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: List of text chunks extracted from the PDF.
    """

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    # Split text into chunks based on paragraphs or other delimiters
    chunks = text.split('\n\n')
    return chunks

def embed_text_chunks(chunks):
    """Embeds text chunks using a pre-trained model.

    Args:
        chunks (list): List of text chunks.

    Returns:
        list: List of embeddings for each chunk.
    """

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    return embeddings

def create_vector_database(embeddings):
    """Creates a FAISS index for efficient similarity search.

    Args:
        embeddings (list): List of embeddings.

    Returns:
        faiss.IndexFlatL2: FAISS index.
    """

    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

# Example usage:
pdf_path = "your_pdf_file.pdf"
chunks = extract_text_from_pdf(pdf_path)
embeddings = embed_text_chunks(chunks)
index = create_vector_database(embeddings)

# To search for similar chunks:
query = "your query text"
query_embedding = model.encode([query])[0]
distances, indices = index.search(query_embedding.reshape(1, -1), k=5)

# Access the top 5 most similar chunks:
for i in indices[0]:
    print(chunks[i])
