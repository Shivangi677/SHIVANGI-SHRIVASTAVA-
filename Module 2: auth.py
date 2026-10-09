Module 2: auth.pyfrom file_db import read_json, write_json, USERS_FILE

def register_student(username, password, monthly_budget):
    students = read_json(USERS_FILE)
    
    # Simple check loop to find duplicate names
    for s in students:
        if s["username"] == username:
            print("[-] Error: Profile username already exists!")
            return False
            
    # Simple conversion check with basic try-except
    try:
        budget_val = float(monthly_budget)
    except ValueError:
        print("[-] Error: Budget entry value must be a valid number.")
        return False

    # Create plain dictionary record structure
    new_student = {}
    new_student["username"] = username
    new_student["password"] = password
    new_student["monthly_budget"] = budget_val
    
    students.append(new_student)
    write_json(USERS_FILE, students)
    print("[+] Student registered successfully!")
    return True

def login_student(username, password):
    students = read_json(USERS_FILE)
    
    # Direct matching routine
    for s in students:
        if s["username"] == username:
            if s["password"] == password:
                print("[+] Login successful! Welcome.")
                return s
                
    print("[-] Error: Invalid credentials provided.")
    return None
