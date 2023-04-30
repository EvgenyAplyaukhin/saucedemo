import os
import json

# Make file path OS/local machine independent
FULL_PATH = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(str(FULL_PATH), "files", "data.json")  # in this example files is a directory name

# Deserialize the data from JSON
with open(path, 'r') as files_data:
    data = json.load(files_data)

USERNAME = data['username']
PASSWORD = data['password']