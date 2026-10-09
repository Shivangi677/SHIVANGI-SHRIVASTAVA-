Module 1: file_db.py
import json
import os

# Standard file naming definitions
USERS_FILE = "student_users.json"
EXPENSES_FILE = "student_expenses.json"

def init_db():
    # Simple check for users file
    if os.path.exists(USERS_FILE) == False:
        f = open(USERS_FILE, "w")
        json.dump([], f)
        f.close()
        
    # Simple check for expenses file
    if os.path.exists(EXPENSES_FILE) == False:
        f = open(EXPENSES_FILE, "w")
        json.dump([], f)
        f.close()

def read_json(file_path):
    try:
        f = open(file_path, "r")
        data = json.load(f)
        f.close()
        return data
    except:
        return []

def write_json(file_path, data):
    f = open(file_path, "w")
    json.dump(data, f, indent=4)
    f.close()
