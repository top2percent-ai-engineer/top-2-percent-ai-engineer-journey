import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "students.json")


if not os.path.exists(FILE_PATH):
    with open(FILE_PATH,"w") as f:
        json.dump({"students": []},f,indent=4)

def load_database():
    with open(FILE_PATH,"r") as f:
        data = json.load(f)
        return data["students"]
    
def view_students():
    students = load_database()
    if not students:
        print("Database is Empty")
        return
    else:
        print("List of all Students")
        for student in students:
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print(f"Email: {student['email']}")
            print("-" * 30)
    
def generate_id(students):
    if not students:
        return 1
    else:
        return max(student["id"] for student in students) + 1

def save_students(students):
    with open(FILE_PATH,"w") as f:
        json.dump({"students": students},f,indent=4)

def add_student():
    print("..... Add New Student .....")
    students = load_database()
    name = input("Student Name: ").strip()
    age = input("Student Age: ").strip()
    email = input("Student Email: ").strip()
    course = input("Student Course: ").strip()
    new_student = {
        "id" : generate_id(students),
        "name" : name,
        "age" : age,
        "email" : email,
        "course" : course
    }
    students.append(new_student)
    save_students(students)
    print(f"Student {name} is added Successfuly!")

def search_student():
    students = load_database()
    name = input("Enter the name to search: ")
    for student in students:
        if (student["name"].lower() == name.lower()):
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print(f"Email: {student['email']}")
            break
    else:
        print("Student not Found!")


def update_student():
    students = load_database()
    id = int(input("Enter the Student ID: "))
    for student in students:
        if (student["id"] == id):
            while True:
                print("Update you want!")
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Email")
                print("4. Update Course")
                print("5. Save Changes and Exit")
                choice = input("Enter the choice: ")
                if not choice.isdigit():
                   print("Must to enter a digit")
                else:
                   choice = int(choice)
                if (choice == 1):
                    name = input("Student Name: ").strip()
                    student["name"] = name
                elif (choice == 2):
                    age = input("Student Age: ").strip()
                    student["age"] = age
                elif (choice == 3):
                    email = input("Student Email: ").strip()
                    student["email"] = email
                elif (choice == 4):
                    course = input("Student Course: ").strip()
                    student["course"] = course
                elif (choice == 5):
                    save_students(students)
                    print("Student Saved Successfully!")
                    break
                else:
                    print("Unclear Entity Selected")
            break
    else:
        print("Student not Found!")
        add_student()


def delete_student():
    students = load_database()
    id = int(input("Enter the Student ID: "))
    for student in students:
        if (student["id"] == id):
            students.remove(student)
            save_students(students)
            print("Student Removed Successfully!")
            break
    else:
        print("Student Already not Exists!")

def show_menue():
    print("Student Record System: ")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    while True:
        show_menue()
        choice = input("Enter choice: ")
        if not choice.isdigit():
            print("Enter Digit ")
            continue
        else:
            choice = int(choice)
        if (choice == 1):
            add_student()
        elif (choice == 2):
            view_students()
        elif (choice == 3):
            search_student()
        elif (choice == 4):
            update_student()
        elif (choice == 5):
            delete_student()
        elif (choice == 6):
            print("Exiting ....")
            break
        else:
            print("Invalid Choice!")

main()