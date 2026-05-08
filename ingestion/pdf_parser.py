from pathlib import Path

RAW_DATA_PATH = Path("../data/raw")

def list_documents():
    files = list(RAW_DATA_PATH.glob("*"))
    return files

if __name__ == "__main__":
    docs = list_documents()
    print("Found documents:")
    for doc in docs:
        print(doc.name)