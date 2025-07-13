import json
import os

def load_data(file_path):
	if not os.path.exist(file_path):
		return []
	try:
		with open(file_path, "r") as file:
			return json.load(file)
	except (FileNotFoundError, json.JSONDecodeError):
		return []

def save_data(file_path, data):
	with open(file_path, "w") as file:
		json.dump(data, file, indent=4)