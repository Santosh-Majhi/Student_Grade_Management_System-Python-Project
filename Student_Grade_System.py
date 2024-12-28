student_marks={}

def add_student(name,mark):
    student_marks[name]= mark
    print(f"Added {name} with a {mark}")

def update_student(name, mark):
    if name in student_marks:
        student_marks[name]= mark
        print(f"{name} with marks are updated {mark}")    
    else:
        print(f"Student {name} is not found!")    

def delete_student(name):
    if name in student_marks:
        del student_marks[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"Student {name} is not found!") 
def display_students():
    if student_marks:
        for name, mark in student_marks.items():
            print(f"{name} : {mark}")
    else:
        print("No student found/added!")



def main():
    while True:
        print("\n Student Grades Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice= int(input("Enter your choice= "))
        if choice == 1:
            name= input("Enter student name= ")
            mark= input("Enter student mark= ")
            add_student(name, mark)

        elif choice ==2:
            name= input("Enter student name= ")
            mark= input("Enter student mark= ")
            update_student(name, mark)
        
        elif choice == 3:
            name= input("Enter student name= ")
            delete_student(name)

        elif choice == 4:
            display_students()    

        elif choice == 5:
            print("Closing the program......")
            break
        else:
            print("Invalid choice") 
main()