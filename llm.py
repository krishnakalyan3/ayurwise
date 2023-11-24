#!/usr/bin/env python

from langchain.llms import AzureOpenAI
from dotenv import load_dotenv
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

load_dotenv(".env")

model = AzureChatOpenAI(
            deployment_name="gpt4",
            openai_api_version="2023-03-15-preview",
        )

message = HumanMessage(
    content="Translate this sentence from English to French. I love programming."
)
print(model([message]))
#print(model(["Tell me a joke"]))
print(model.invoke("abc"))





DATABASE_PATH = os.environ.get("DATABASE_PATH")

query = "what is ayuerveda"
#embedding_function = OpenAIEmbeddings(engine="gpt4")
embedding_function: OpenAIEmbeddings = OpenAIEmbeddings(
    openai_api_base= os.environ.get("OPENAI_API_BASE"),
    openai_api_type='azure',
    deployment='text-embedding-ada-002',
    openai_api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
    chunk_size=1,
)

vectorstore = Chroma(persist_directory=DATABASE_PATH, embedding_function=embedding_function)
#retriever = vectorstore.as_retriever()

query = "What did the president say about Ketanji Brown Jackson"
docs = vectorstore.similarity_search(query)
print(docs)



#v = db.similarity_search(query)
from langchain.prompts import ChatPromptTemplate

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

prompt = ChatPromptTemplate.from_template(template)
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)
a = chain.invoke("where did harrison work?")
print(a)
