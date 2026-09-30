from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)


def coder_agent(plan: str, architecture: str,project_analysis:str):
    prompt = f"""
You are a senior software developer agent.

Your job is to implement the software based on the provided
implementation plan and technical architecture.
EXISTING PROJECT ANALYSIS:
{project_analysis}

IMPLEMENTATION PLAN:
{plan}

TECHNICAL ARCHITECTURE:
{architecture}

For now, do NOT modify files directly.

Instead, provide:
1. Files that need to be created
2. Files that need to be modified
3. What each file should contain
4. Important implementation details
5. Dependencies required
6. Potential implementation issues

Focus on translating the architecture into concrete implementation work.
"""

    response = llm.invoke(prompt)

    return response.text
