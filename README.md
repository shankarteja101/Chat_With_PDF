# Chat_With_PDF
Sitafal_TASK_1
Task 1: Chat with PDF Using RAG Pipeline
Overview
This task involves creating a Retrieval-Augmented Generation (RAG) system to process and interact with semi-structured PDF data. The solution focuses on extracting, chunking, embedding, and storing data for efficient retrieval to answer user queries accurately.

Steps to Solve
Data Ingestion

Extract text and structured information from PDF files using text extraction tools.
Segment the extracted data into smaller, logical chunks for better context management.
Convert these chunks into vector embeddings using a pre-trained embedding model.
Store the generated embeddings in a vector database for fast similarity-based retrieval.
Query Handling

Transform the user’s query into vector embeddings using the same embedding model.
Conduct a similarity search within the vector database to retrieve the most relevant data chunks.
Pass the retrieved content to the language model, combining it with a prompt to generate a detailed response.
Comparison Queries

Identify the key fields or terms mentioned in the query for comparison (e.g., unemployment rates).
Retrieve related data chunks from the vector database and extract the necessary information.
Process and organize the extracted details into a structured format, such as a table or bullet points, for clear comparisons.
Response Generation

Leverage the language model to produce a context-aware, factual response using the retrieved content.
Ensure the response directly incorporates data from the retrieved chunks to maintain accuracy.
Example Solutions
Page 2: Extract specific unemployment rates based on degree types using precise methods.
Page 6: Retrieve and present tabular data accurately for user queries.
