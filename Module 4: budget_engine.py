Module 4: budget_engine.pyfrom tracker import get_student_expenses

def calculate_budget_status(username, monthly_budget):
    expenses = get_student_expenses(username)
    
    # Simple accumulator loop to sum up expenses
    total_spent = 0.0
    for e in expenses:
        total_spent = total_spent + e["amount"]
        
    remaining_balance = monthly_budget - total_spent
    
    # Standard conditional arithmetic calculation
    if monthly_budget > 0:
        percent_spent = (total_spent / monthly_budget) * 100.0
    else:
        percent_spent = 0.0
        
    # Straightforward conditional branching hierarchy (if-elif-else)
    alert = "SAFE"
    if total_spent >= monthly_budget:
        alert = "CRITICAL: OVER BUDGET!"
    elif percent_spent >= 80.0:
        alert = "WARNING: Spent over 80% of allowance!"
        
    # Return explicit summary collection dictionary with single decimal precision
    status = {}
    status["total_budget"] = monthly_budget
    status["total_spent"] = total_spent
    status["remaining_balance"] = remaining_balance
    status["percent_spent"] = round(percent_spent, 1)
    status["alert_status"] = alert
    
    return status
