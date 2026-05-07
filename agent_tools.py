from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.agents import AgentType

load_dotenv()

# Tool function
def calculator_tool(query):
    return str(eval(query))

# Register tool
tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for performing math calculations"
    )
]

# Initialize Groq model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0
)

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Invoke agent
response = agent.invoke(
    "What is 45 * 12?"
)

print("\nAgent Response:\n")
print(response)