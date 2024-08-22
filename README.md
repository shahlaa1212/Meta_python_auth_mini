# 🔐 Authentication Functions in Python 
![python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) 
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) 
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) 
![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)

# 🧾 Overview
This project is part of a Back-End Development course focusing on Week 1 of the "Programming with Python" module. The task involves implementing basic authentication functions, including user sign-in, sign-up, and sign-out, using Python. The project emphasizes both fundamental Python programming using procedure function and csv file 

# 📅 Course Context
- Course: Meta Backend Developer Specialization
- Module: Programming with Python
- Week: 1
- Focus: Python fundamentals, file handling, user authentication

# 📖 Task Description
## **Objective**

The objective of this task is to create a Python program that handles basic user authentication through command-line interactions. Users can sign up, sign in, and sign out, with all user data stored in a CSV file. The program ensures that user data is properly validated and securely managed.
Key Features

- Sign Up: Users can create a new account by providing their first name, last name, username, password, and age. The program validates that the username is unique and ensures that the password is not empty and the age is a positive integer.
- Sign In: Users can log in by providing a valid username and password. The program checks if the credentials match and updates the user's login status.
- Sign Out: Logged-in users can log out, and the program will update their login status accordingly.

## **File Structure**

- main.py: Handles user input from the command line and manages the program's flow.
- auth.py: Contains the pure functions (signup, signin, signout) that handle the core authentication logic.
- users.csv: Stores user data, with fields for first name, last name, username, password, age, and login status.

## **Key Concepts**

- Pure Functions: The task is designed to encourage the use of pure functions, which operate on the given input and produce output without side effects.
- File Handling: User data is read from and written to a CSV file, providing a practical introduction to file I/O in Python.
- OOP Principles: While the task avoids a full object-oriented design (i.e., no UserManager class), it still demonstrates modularity and the organization of related functions and data.

# 📌 **Getting Started**
## Prerequisites
- Python 3.x
- Basic knowledge of Python programming
- Familiarity with command-line interface (CLI) operations

## Running the Program  
1. **Clone the repository:**
 ```sh
  git clone https://github.com/yourusername/authentication-python-task.git
```
```sh
  cd authentication-python-task
```
2. **Run the main program:**
```sh
  python main.py
```
3. Follow the on-screen prompts to sign up, sign in, or sign out.

# 🤝 Conclusion
This project serves as an introduction to backend development using Python, focusing on user authentication and file handling. It lays the groundwork for more complex tasks in the subsequent weeks of the course.

