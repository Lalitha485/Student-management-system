## Student Management System

## Description
Console-based Student Management System written in Python.
Performs CRUD operations (Create, Read, Update, Delete) and stores data in `students.json`.

## Files
- `main.py` : Application code
- `students.json` : Data file (created automatically)

## How to run
1. Make sure you have Python 3 installed.
2. Place `main.py` and (optional) `students.json` in the same folder.
3. Run:
```
python main.py
```

## Features
- Add new student (prevents duplicate IDs)
- View all students
- Search student by ID
- Update student (keep existing value by leaving input blank)
- Delete student with confirmation

## GitHub Upload Steps
1. Create repository on GitHub named `Student-Management-System`.
2. In project folder:
```
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_REPO_URL
git push -u origin main
```
Or use GitHub web upload: `Add file -> Upload files`.

## What to explain in interview
- Tech used: Python, JSON
- Key concepts: File handling, JSON, modular functions, input validation, CRUD
- Improvements for next version: SQLite or MySQL integration, web frontend (Flask/Django), validation for fields, unit tests.
