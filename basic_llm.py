from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize Groq model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.7
)

# Invoke model
response = llm.invoke(
    "Explain LangChain in one paragraph"
)

# Print output
print("\nResponse:\n")
print(response.content)