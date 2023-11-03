import chromadb


# Create ChromaDB client
chroma_client = chromadb.PersistentClient(path=".db_local")

# Get the collection named "my_collection"
collection = chroma_client.get_collection(name="my_collection")

# Query the collection
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

# Print results
print(results)
