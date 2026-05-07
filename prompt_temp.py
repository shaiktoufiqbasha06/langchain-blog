from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

# Initialize model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

# Prompt template
template = PromptTemplate.from_template(
    "Explain {topic} in simple terms"
)

# Generate prompt
prompt = template.invoke({
    "topic": "Vector Databases"
})

# Invoke model
response = llm.invoke(prompt.text)

print("\nGenerated Response:\n")
print(response.content)