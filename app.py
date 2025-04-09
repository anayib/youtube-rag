from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from retriver import retrieve_context
from prompt import prompt

# Initialize the LLM
model = ChatOllama(model="llama3.2")
parser = StrOutputParser()

# Create the chain with retrieval
def process_query(input_dict):
    # Get the question from the input
    question = input_dict["question"]
    # Retrieve relevant context
    context = retrieve_context(question)
    # Return both for the prompt
    return {"context": context, "question": question}

#Get user question
question = input("Enter your question: ")

# Build the chain
chain = (
    RunnablePassthrough.assign(processed=process_query)
    | (lambda x: {"context": x["processed"]["context"], "question": x["processed"]["question"]})
    | prompt
    | model
    | parser
)

# Example usage
answer = chain.invoke({"question": question})
print(f"Question: {question}")
print(f"Answer: {answer}")
