from graph.workflow import app


result = app.invoke({
    "user_request": "Build a FastAPI todo application",
    "project_content": "This is a new project. No existing code.",
    "project_analysis": "",
    "plan": "",
    "architecture": "",
    "code_plan": ""
})


print("=== PROJECT ANALYSIS ===")
print(result["project_analysis"])

print("\n=== PLANNER OUTPUT ===")
print(result["plan"])

print("\n=== ARCHITECT OUTPUT ===")
print(result["architecture"])

print("\n=== CODER OUTPUT ===")
print(result["code_plan"])