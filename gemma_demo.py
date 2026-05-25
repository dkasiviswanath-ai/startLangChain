from langchain_community.llms import Ollama

llm = Ollama(model="gemma:2b")

question = input("What is your question? ")
response = llm.invoke(question)

print(response)
