from src.helper import *
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


extracted_data = load_pdf("./data")
text_chunks = text_split(extracted_data=extracted_data)
embeddings = download_hugging_face_embedding()

index_name = "medical-chatbot"

vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
vectorstore.from_texts([t.page_content for t in text_chunks], index_name=index_name, embedding=embeddings)
