import json

class StudentStorage:
    def __init__(self, fname = "student.json"):
        self.fname = fname
    
    def readata(self):
        try:
            with open(self.fname, "r") as f:
                return json.load(f)
        except:
            return {}
    
    def writedata(self, data):
        with open(self.fname, "w") as f:
            json.dump(data, f)

class StudentManager:
    def __init__(self, storage):
        self.storage = storage
        self.students = self.storage.readata()
    
    def add(self, name, grade):
        self.students[name] = grade
        self.storage.writedata(self.students)
    
    def rem(self, name):
        if name in self.students:
            del self.students[name]
            self.storage.writedata(self.students)
            return True
        else:
            return None
    
    def disp(self):
        return self.students
    
    def ave(self):
        if self.students == {}:
            return None
        else:
            return sum(self.students.values())/len(self.students)
    
    def topper(self):
        if self.students == {}:
            return None
        else:
            return [(n,g) for n, g in self.students.items() if g == max(self.students.values())]

sto = StudentStorage()
std = StudentManager(sto)

print("\tStudent Grade Manager")

while True:
    print("\nMenu\n 1.Add\n 2.Remove\n 3.Display All\n 4.Average Grade\n 5.Highest Scorer\n 6.Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Name: ")
        try:
            grade = float(input("Grade: "))
        except:
            print("Invalid Grade!")
        else:
            std.add(name, grade)
            print("Added")
    
    if choice == "2":
        name = input("Name: ")
        if std.rem(name):
            print("Removed")
        else:
            print("Error remvoing data")
    
    if choice == "3":
        if std.disp():
            print("Name\tGrade")
            for name, grade in std.disp().items():
                print(name, "\t", grade)
        else:
            print("No Student Data Added")
    
    if choice == "4":
        print("Average:", std.ave())
    
    if choice == "5":
        if std.topper():
            print("Topper is", std.topper())
        else:
            print("No Student Data Added")
    
    if choice == "6":
        print("\nGOOD BYE")
        break
    
    