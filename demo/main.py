from dotenv import load_dotenv
load_dotenv()
from orchestrator import assign_task

task = input("Enter task: ")

result = assign_task(task)

print("\nGenerated Result:\n")
print(result)