import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama  # Updated import
#from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
parser = StrOutputParser()
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = ChatOllama(model="llama3.2")#ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0)

template = """
Answer the question based on the context provided below. if you don't know the answer, just say "I don't know".

Context: {context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model | parser

print (chain.invoke({
  "context": "The capitla of France is Paris",
  "question": "What is the capital of France?"
}))

