from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)


def project_analyzer(project_content: str):
    prompt = f"""
You are a software project analysis agent.

Analyze the existing project information provided below.

PROJECT CONTENT:
{project_content}

Identify:

1. Project purpose
2. Existing project structure
3. Technologies and frameworks
4. Main components
5. Current architecture
6. Existing functionality
7. Potential bugs or code quality issues
8. Missing features
9. Security concerns
10. Testing status
11. Improvement opportunities

Do not modify any files.
Do not write implementation code.

Return a clear technical analysis that another planning agent can use.
"""

    response = llm.invoke(prompt)

    return response.text