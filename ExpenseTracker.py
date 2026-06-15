import json

class ExpenseStorage:
    def __init__(self, fname = "expense.json"):
        self.fname = fname
    
    def read_expense(self):
        try:
            with open(self.fname, "r") as f:
                return json.load(f)
        except:
            return []
    
    def write_expense(self, expense):
        with open(self.fname, "w") as f:
            json.dump(expense, f, indent=3)

class ExpenseTracker:
    def __init__(self, storage):
        self.storage = storage
        self.expense_data = self.storage.read_expense()
    
    def add_expense(self, ids, item, category, amount):
        data = {"id":ids, "item": item, "category": category, "amount": amount}
        self.expense_data.append(data)
        self.storage.write_expense(self.expense_data)
    
    def remove_expense(self, item):
        for i, x in enumerate(self.expense_data):
            if item in x.values():
                del self.expense_data[i]
                self.storage.write_expense(self.expense_data)
                return True
        return False
    
    def spending(self):
        total = 0.0
        if self.expense_data:
            for expense in self.expense_data:
                total += expense["amount"]
            return total
        return None
    
    def display(self, category=""):
        item_list= []
        if not category:
            return self.expense_data
        for item in self.expense_data:
            if item["category"] == category:
                item_list.append(item)
        return item_list
    
    def category_summary(self):
        cat = {}
        for item in self.expense_data:
            if item["category"] in cat:
                cat[item["category"]] += item["amount"]
            else:
                cat[item["category"]] = item["amount"]
        return cat


exs = ExpenseStorage()
ext = ExpenseTracker(exs)

print("\tExpense Tracker")
while True:
    print("\nMenu\n 1.Add Expense\n 2.Remove Expense\n 3.Display All Expense\n \
4.Total Spending\n 5.Display By Category\n 6.Category Summary\n 7.Exit")
    choice = input("Enter your choice: ")
    ids = 1
    def disp(expense):
        print("\n{:<5}{:<12}{:<15}{:<10}".format("No", "Category", "Item", "Amount"))
        print("-" * 45)

        for i, item in enumerate(expense, start=1):
            print("{:<5}{:<12}{:<15}{:<10}".format(i, item["category"], item["item"], item["amount"]))

    if choice == "1":
        item = input("Item: ").title()
        category = input("Category: ").title()
        try:
            amount = float(input("Amount: "))
        except:
            print("##Invalid Amount!##")
            continue
        else:
            ext.add_expense(ids, item, category, amount)
            ids += 1
            print("**Added**")

    elif choice == "2":
        item = input("Item: ").title()
        
        if ext.remove_expense(item):
            print(f"**Item {item} removed**")
        else:
            print("##No such item added##")

    elif choice == "3":
        expense = ext.display()
        disp(expense)

    elif choice == "4":
        total = ext.spending()
        if total:
            print("Total Spending:", total)
        else:
            print("No expense added yet")

    elif choice == "5":
        category = input("Enter category: ").title()
        item_list = ext.display(category)
        disp(item_list)
        

    elif choice == "6":
        print("\n{:<12}{:<15}".format("Category", "Amount"))
        print("-" * 20)

        for key, val in ext.category_summary().items():
            print("{:<12}{:<15}".format(key, val))
    
    elif choice == "7":
        break
    
    else:
        print("Invalid choice")