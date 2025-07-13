import argparse
from models.user import User
from models.task import Task
from models.project import Project

# Global dictionary to store users, projects, and tasks
users = {}
projects = {}
tasks = {}

def add_user(args):
    if args.name in users:
        print(f"User, '{args.name}' already exists.")
        return
    user = User(args.name, args.email)
    users[args.name] = user
    print(f"User added: {user}")

def add_project(args):
    user = users.get(args.user) or User(args.user)
    if not user:
        print(f"User '{args.user}' not found.")

    project = Project(args.title, args.description, args.due_date)
    user.add_project(project)  
    projects[args.title] = project
    print(f"Project added: {project}")

def add_task(args):
    project = projects.get(args.project)
    if not project:
        print(f"Project '{args.project}' not found.")
        return
    
    task = Task(args.title, args.status, args.assigned_to)
    project.add_task(task)     
    task[args.title] = task
    print(f"Task added to project- {args.project} : {task}")

def list_projects(args):
    user = users.get(args.user)
    if not user:
        print(f"User '{args.user}' not found.")
    if not user.projects:
        print(f"No projects for user '{args.user}'.")
        return

    print(f"Projects for {args.user}:")
    for proj in user.projects:
        print(f"{proj.title} is due {proj.due_date}")

def complete_task(args):
    task = task.get(args.title)
    if not task:
        print(f"Task '{args.title}' not found.")
        return
    task.complete()
    print(f"Task '{args.task}' is complete!")

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers()
    
	# Subparser for add user
    add_parser = subparsers.add_parser("add-user", help="Add a new user")
    add_parser.add_argument("name")
    add_parser.add_argument("email")
    add_parser.set_defaults(func=add_user)
    
	# Subparser for add project
    add_parser = subparsers.add_parser("add-project", help="Add a new project")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.add_argument("status")
    add_parser.add_argument("assigned-to")
    add_parser.set_defaults(func=add_project)
    
	# Subparser for add task
    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("project")
    add_parser.add_argument("title")
    add_parser.add_argument("description")
    add_parser.add_argument("due-date")
    add_parser.set_defaults(func=add_task)  
    
	# Subparser for listing projects
    list_parser = subparsers.add_parser("list-projects", help="Lists projects for user")
    list_parser.add_argument("user")
    list_parser.set_defaults(func=list_projects)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
   
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
