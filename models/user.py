from project import Project

class User:
	all_users = []

	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.projects = []

		User.all_users.append(self)

	def add_projects(self, project):
		if isinstance(project, Project):
			self.projects.append(project)
		else:
			raise ValueError("Invalid project")

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self,value):
		if isinstance(value, str) and len(value) <= 15:
			self._name = value
		else:
			raise ValueError("Name must be a string and not exceed 15 characters")

	def __repr__(self):
		return f"User: {self.name}, Projects: {len(self.projects)}"

	def get_project_by_title(self, title):
		for project in self.projects:
			if project.title == title:
				return project
		return None

	@classmethod
	def all_users(cls):
		return cls.all_users








	