# 🔐 Authentication Functions in Python 
![python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) 
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) 
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) 
![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)

## 🧾 **Overview**
This project is part of a Back-End Development course focusing on Week 1 of the "Programming with Python" module. The task involves implementing basic authentication functions, including user sign-in, sign-up, and sign-out, using Python. The project emphasizes both fundamental Python programming using procedure function and csv file 

## 📅 **Course Context**
- Course: Meta Backend Developer Specialization
- Module: Programming with Python
- Week: 2
- Focus: Python fundamentals, file handling, user authentication

## 📖 **Task Description**
### **Objective**

In this task, you will implement basic authentication functions for a Python program that handles user sign-in, sign-up, and sign-out. You will be working with user data stored in a file (**users.csv** or **users.txt**). The goal is to read, write, and update user data through command-line interactions. The data in the file will be structured as follows:
```sh
 first_name, last_name, username, password, age, is_loggedin
```
- Sign Up: Users can create a new account by providing their first name, last name, username, password, and age. The program validates that the username is unique and ensures that the password is not empty and the age is a positive integer.
- Sign In: Users can log in by providing a valid username and password. The program checks if the credentials match and updates the user's login status.
- Sign Out: Logged-in users can log out, and the program will update their login status accordingly.

## **File Structure**

- **main.py** : This file will handle user input from the command line and manage the flow of the program.
- **auth.py** : This file will contain the authentication functions for sign-in, sign-up, and sign-out.
- users.csv: Stores user data, with fields for first name, last name, username, password, age, and login status.

## **Implement Functions :-**
- ### **signup()**
- [ ] Prompt the user for **first_name**, **last_name**, **username**, **password**, and **age**.
- [ ] Validate that **username** does not already exist in the data file.
- [ ] If the username** is unique, append the new user's data to the file with **is_loggedin** set to **False**.
- [ ] Print a success message after a successful sign-up.
- [ ] If the username already exists, print an error message and ask the user to try again.

- ### **signin()**
- [ ] Prompt the user for username and password.
- [ ] Read the data file and check if the username and password match an existing record.
- [ ] If the credentials are correct, update the is_loggedin status to True for that user.
- [ ] Print a success message after a successful login.
- [ ] If the credentials are incorrect, print an error message and ask the user to try again.

- ### **signout()**
- [ ] Prompt the user for **username**.
- [ ] Read the data file and check if the user is currently logged in (**is_loggedin** is **True**).
- [ ] If the user is logged in, update the **is_loggedin** status to **False**.
- [ ] Print a success message after a successful logout.
- [ ] If the user is not logged in, print an error message.

## 📌 **Getting Started**
### Prerequisites
- Python 3.x
- Basic knowledge of Python programming
- Familiarity with command-line interface (CLI) operations

### Running the Program  
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

## 🤝 **Conclusion**
This project serves as an introduction to backend development using Python, focusing on user authentication and file handling. It lays the groundwork for more complex tasks in the subsequent weeks of the course.

