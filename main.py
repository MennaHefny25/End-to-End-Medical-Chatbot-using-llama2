import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embedding
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from src.prompt import * 

MODEL_PATH = "./model/llama-2-7b-chat.ggmlv3.q4_0.bin"


app = Flask(__name__)


load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

embeddings = download_hugging_face_embedding()

index_name = "medical-chatbot"

vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)


PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)


llm = CTransformers(
    model=MODEL_PATH,
    model_type="llama",
    config={
        "max_new_tokens": 512,
        "temperature": 0.8,
    },
)


# Initialize the RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever = vectorstore.as_retriever(search_kwargs={"k":2}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])


if __name__ == '__main__':
    app.run(host="localhost", port= 5000, debug= True)