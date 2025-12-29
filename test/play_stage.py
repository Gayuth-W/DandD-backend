from app.core.database import SessionLocal
from app.models.project import Project
from app.models.task import Task
from app.models.user import User

db = SessionLocal()

proj = db.query(Project).filter(Project.name == "Test Project").first()
if proj:
    for task in proj.tasks:
        print(f"Stage {task.stage}: {task.title} | {task.text} | Keywords: {task.keywords}")
else:
    print("Project not found")
    
user = db.query(User).filter(User.email == "test@example.com").first()

# Let's say the user enters some input
user_input = "defeat the dragon and save the village"

# Fetch tasks for the user's project for stage 1
tasks_stage_1 = db.query(Task).filter(Task.project_id == user.project_id, Task.stage == 1).all()

for task in tasks_stage_1:
    if task.keywords and any(word in user_input for word in task.keywords.split(",")):
        print("Matched Task:", task.text)
    else:
        print("No match for this task")
        
user.t_score += tasks_stage_1[0].score  # Example: add score of matched task
db.commit()
print("Updated score:", user.t_score)            