from task import Task
from datetime import datetime

class Project:
	def __init__(self, title, description, due_date):
		self.title = title
		self.description = description
		self.due_date = due_date
		self.tasks = []

	def add_task(self, task):
		self.tasks.append(task)

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, value):
		if isinstance(value, str) and value.strip():
			self._title = value
		else:
			raise ValueError
		
	@staticmethod
	def _validate_due_date(due_date):
		try:
			return datetime.strptime(due_date, "%Y-%m-%d")
		except:
			raise ValueError("Due date must be in YYYY-MM-DD format")

	def __repr__(self):
		return f"Project: {self.title}, Due: {self.due_date}, Tasks: {len(self.tasks)}"