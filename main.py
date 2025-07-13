import argparse
from models.user import User
from models.task import Task
from models.project import Project

# Global dictionary to store users and their tasks
users = {}

def add_user(args):
	pass

# def add_user(self,name, email):
	# 	new_user = {
	# 		"name": name,
	# 		"email": email
	# 	}
	# 	self.user.append(new_user)

def add_project(args):
      pass

def add_task(args):
	pass      

def list_projects(args):
    pass

def complete_task(args):
	pass
    

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
