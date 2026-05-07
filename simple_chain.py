from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Initialize model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

# Prompt
prompt = ChatPromptTemplate.from_template(
    "Write 5 important points about {topic}"
)

# Chain
chain = prompt | llm

# Run chain
response = chain.invoke({
    "topic": "AI Agents"
})

print("\nChain Output:\n")
print(response.content)