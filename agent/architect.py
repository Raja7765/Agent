from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)


def architect_agent(plan: str,project_analysis:str):
    prompt = f"""
You are a software architect agent.

Based on the implementation plan below, design the technical architecture
for the software project.

Implementation Plan:
{plan}

Provide:

1. Overall architecture
2. Project folder structure
3. Main components and their responsibilities
4. API design
5. Database design
6. Data flow
7. Technology choices
8. Important technical decisions
9. Potential architecture risks

Do not write implementation code.
Focus only on architecture and design.
"""

    response = llm.invoke(prompt)

    return response.text
