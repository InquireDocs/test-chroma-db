import chromadb


# Create ChromaDB client
chroma_client = chromadb.PersistentClient(path=".db_local")

#  Create a collection named "my_collection"
collection = chroma_client.create_collection(name="my_collection")

# Write to the collection
collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)
