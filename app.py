import os
from typing import List

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import XinferenceEmbeddings
from langchain.vectorstores import Milvus


def load_documents_from_directory(directory_path: str) -> List[str]:
    files_path = []
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".txt"):
            print(f"file_name: {file_name}")
            file_path = os.path.join(directory_path, file_name)
            files_path.append(file_path)
    return files_path


# Replace the previous code with the following:

directory_path = "./docs"  # Replace with the actual directory path

files_path = load_documents_from_directory(directory_path)

documents = []
for file_path in files_path:
    print(f"file_path: {file_path}")
    loader = TextLoader(file_path)  # 替换成任何你想要进行问答的txt文件
    document = loader.load()
    documents.extend(document)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=100,
    length_function=len,
)
docs = text_splitter.split_documents(documents)
print(f"len(docs): {len(docs)}")

xinference_embeddings = XinferenceEmbeddings(
    server_url="http://127.0.0.1:9997",  # 换成设置的url，这里用的是默认端口
    # 替换成之前返回的Falcon-Instruct模型model_uid
    model_uid="6a03df94-407f-11ee-85bc-00155d1e0dda"
)

vector_db = Milvus.from_documents(
    docs,
    xinference_embeddings,
    connection_args={"host": "127.0.0.1", "port": "19530"},
)

query = "本科生到校路费没凑齐怎么办？"
results = vector_db.similarity_search(query, k=3)
print(results)
print(results[0].page_content)
