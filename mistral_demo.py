from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

question = input("What is your question? ")
response = llm.invoke(question)

print(response)
