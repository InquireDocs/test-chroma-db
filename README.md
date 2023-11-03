# Test Chroma DB

This is a simple project to test [Chroma DB](https://www.trychroma.com/) on a local environment as part of Python app.

1. Create a Python virtual environment
```bash
virtualenv env
source env/bin/activate
```

2. Update Pip and install dependencies
```bash
pip install --upgrade pip
pip install --requirement requirements.txt
```

3. Use the `write.py` script to write to the database stored locally in a file
```bash
python write.py
```

4. Use the `read.py` script to make a query to the database
```bash
python read.py
```

Expected output:
```bash
{'ids': [['id1', 'id2']], 'distances': [[0.7111213785443223, 1.010977553098025]], 'metadatas': [[{'source': 'my_source'}, {'source': 'my_source'}]], 'embeddings': None, 'documents': [['This is a document', 'This is another document']]}
```
