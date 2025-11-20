"""
Student Management System (Console-based)
Author: Generated for user
Description: Simple CRUD app using JSON for persistence.
"""

import json
import os

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    data = load_data()
    student = {}
    student["id"] = input("Enter Student ID: ").strip()
    # Avoid duplicate IDs
    if any(s["id"] == student["id"] for s in data):
        print("ID already exists. Use update if you want to change details.\n")
        return
    student["name"] = input("Enter Student Name: ").strip()
    student["age"] = input("Enter Age: ").strip()
    student["course"] = input("Enter Course: ").strip()
    data.append(student)
    save_data(data)
    print("Student Added Successfully!\n")

def view_students():
    data = load_data()
    if not data:
        print("No students found\n")
        return
    print("\n--- Student Records ---")
    for s in data:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
    print()

def search_student():
    data = load_data()
    sid = input("Enter Student ID to Search: ").strip()
    for s in data:
        if s["id"] == sid:
            print("\n--- Student Found ---")
            print(f"ID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")
            print(f"Course: {s['course']}\n")
            return
    print("Student Not Found\n")

def update_student():
    data = load_data()
    sid = input("Enter Student ID to Update: ").strip()
    for s in data:
        if s["id"] == sid:
            name = input(f"Enter New Name (leave blank to keep '{s['name']}'): ").strip()
            age = input(f"Enter New Age (leave blank to keep '{s['age']}'): ").strip()
            course = input(f"Enter New Course (leave blank to keep '{s['course']}'): ").strip()
            if name:
                s["name"] = name
            if age:
                s["age"] = age
            if course:
                s["course"] = course
            save_data(data)
            print("Student Updated Successfully\n")
            return
    print("Student Not Found\n")

def delete_student():
    data = load_data()
    sid = input("Enter Student ID to Delete: ").strip()
    for s in data:
        if s["id"] == sid:
            confirm = input(f"Are you sure you want to delete {s['name']} (y/n)? ").lower()
            if confirm == 'y':
                data.remove(s)
                save_data(data)
                print("Student Deleted Successfully\n")
            else:
                print("Delete cancelled\n")
            return
    print("Student Not Found\n")

def menu():
    while True:
        print("------ Student Management System ------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid Input! Try again.\n")

if __name__ == '__main__':
    menu()
