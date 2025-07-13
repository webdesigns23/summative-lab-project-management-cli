class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.projects = []

	def add_projects(self, project):
		self.projects.append(project)

	def __repr__(self):
		return f"User: {self.name}, Projects: {len(self.projects)}"

	@classmethod
	def all_users(cls):
		return cls.all_users

	def get_project_by_title(self, title):
		for project in self.projects:
			if project.title == title:
				return project
			else:
				return None








	