Module 3: tracker.pyfrom file_db import read_json, write_json, EXPENSES_FILE

def add_expense(username, amount, category, description):
    try:
        amount_val = float(amount)
    except ValueError:
        print("[-] Error: Cost value must be a valid float.")
        return False
        
    expenses = read_json(EXPENSES_FILE)
    
    # Store dynamic entry values into standard dictionary maps
    new_expense = {}
    new_expense["username"] = username
    new_expense["amount"] = amount_val
    new_expense["category"] = category
    new_expense["description"] = description
    
    expenses.append(new_expense)
    write_json(EXPENSES_FILE, expenses)
    print("[+] Expense logged successfully!")
    return True

def get_student_expenses(username):
    all_expenses = read_json(EXPENSES_FILE)
    student_list = []
    
    # Basic filtering using standard append loop
    for e in all_expenses:
        if e["username"] == username:
            student_list.append(e)
            
    return student_list
