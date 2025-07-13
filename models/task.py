class Task:
	def __init__(self, title, completed=False, assigned_to=None):
		self.title = title
		self.completed = completed
		self.assigned_to = assigned_to

	def update_status_completed(self):
		self.completed = True
		
	def __repr__(self):
		status = "yes" if self.completed else "no"
		return f"{status} {self.title}"