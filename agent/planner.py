from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)


def planner_agent(user_request: str):
    prompt = f"""
You are a software project planning agent.

Analyze the user's software request and create a clear implementation plan.

User request:
{user_request}

Provide:
1. Requirements
2. Main components
3. Implementation steps
4. Technologies needed
5. Potential challenges
"""

    response = llm.invoke(prompt)

    return response.text