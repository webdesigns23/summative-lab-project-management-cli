class Task:
	def __init__(self, title, status=False, assigned_to=None):
		self.title = title
		self.status = status
		self.assigned_to = assigned_to

	def task_completed(self):
		self.status = True
		print(f"Task '{self.title}' completed.")

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, value):
		if isinstance(value, str) and len(value) <= 50:
			self._description = value
		else:
			raise ValueError("Description must be a sring that does not exceed 50 characters")
	
	def __repr__(self):	
		status = "Completed" if self.status else "Incomplete"	
		return f"Task: {self.title}, Assigned to: {self.assigned_to}, Status: {status}"