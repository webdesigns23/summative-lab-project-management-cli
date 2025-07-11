class Task:
	def __init__(self, title, status=False, assigned_to=None):
		self.title = title
		self.status = status
		self.assigned_to = assigned_to