class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email

	def add_user(self,name, email):
		new_user = {
			"name": name,
			"email": email
		}
		self.user.append(new_user)