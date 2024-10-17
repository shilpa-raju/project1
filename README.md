# personal to-do list 
# Personal To-Do List Application

## Objective
Develop a Personal To-Do List Application that allows users to create, view, edit, and delete tasks with a focus on user interaction and file handling without using databases.

## Features
- **Task Management**: 
  - Add tasks with a title, description, and category.
  - Mark tasks as completed or delete them.
- **Categorization**: 
  - Categorize tasks (e.g., Work, Personal, Urgent).
- **Persistence**: 
  - Store tasks in a local JSON file to save progress between sessions.

## Project Structure
```plaintext
/todo_app
├── todo.py          # Main application logic
├── tasks.json       # File to store tasks
└── README.md        # Documentation
