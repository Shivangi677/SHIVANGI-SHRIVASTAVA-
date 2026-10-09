Module 5: main.pyfrom file_db import init_db
import auth
import tracker
import budget_engine

def start_app():
    init_db()
    current_session = None
    
    while True:
        print("\n=============================================")
        print("     CAMPUS BUDGET & EXPENSE TRACKER v1.0    ")
        print("=============================================")
        
        if current_session == None:
            print("1. Register Student Account")
            print("2. Student Login")
            print("3. Exit System")
            choice = input("Enter choice (1-3): ")
            
            if choice == "1":
                user = input("Choose Username: ")
                pwd = input("Choose Password: ")
                budget = input("Enter Monthly Pocket Money Allowance (₹): ")
                auth.register_student(user, pwd, budget)
            elif choice == "2":
                user = input("Username: ")
                pwd = input("Password: ")
                current_session = auth.login_student(user, pwd)
            elif choice == "3":
                print("[*] Exiting application. Goodbye!")
                break
        else:
            print("\n[Logged In As: " + str(current_session['username']) + "]")
            print("1. Log a Daily Expense")
            print("2. View Expense History Log")
            print("3. Check Budget Analytics Status")
            print("4. Logout")
            choice = input("Enter choice (1-4): ")
            if choice == "1":
                amt = input("Enter Amount spent (₹): ")
                print("Categories: Food, Books, Rent, Canteen, Entertainment, Travel")
                cat = input("Enter Category: ")
                desc = input("Short Description: ")
                tracker.add_expense(current_session["username"], amt, cat, desc)
                
            elif choice == "2":
                history = tracker.get_student_expenses(current_session["username"])
                if len(history) == 0:
                    print("[-] No expenses logged yet.")
                else:
                    print("\n--- EXPENSE HISTORY LOG ---")
                    print("Category | Amount | Description")
                    print("---------------------------------")
                    # Simple loop to print text sequentially without advanced alignment spacing strings
                    for e in history:
                        print(str(e['category']) + " | ₹" + str(e['amount']) + " | " + str(e['description']))
                        
            elif choice == "3":
                status = budget_engine.calculate_budget_status(
                    current_session["username"], 
                    current_session["monthly_budget"]
                )
                print("\n================ BUDGET ANALYTICS ================")
                print("Total Allowance Assigned : ₹" + str(status['total_budget']))
                print("Total Capital Consumed   : ₹" + str(status['total_spent']))
                print("Remaining Wallet Balance : ₹" + str(status['remaining_balance']))
                print("Percentage Consumed     : " + str(status['percent_spent']) + "%")
                print("System Security Status   : " + str(status['alert_status']))
                print("==================================================")
                
            elif choice == "4":
                current_session = None
                print("[*] Session terminated successfully.")

if __name__ == "__main__":
    start_app()

           
