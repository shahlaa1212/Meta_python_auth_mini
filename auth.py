# Define the file name (can be .csv or .txt)
import csv
FILE_NAME = 'users.csv'

# Function to sign up a new user
def signup():
    # Gather user input
    first_name = input("Enter The first_name: ")
    last_name = input("Enter The last_name: ")
    username = input("Enter The username: ") 
    password = input("Enter The password: ") 
    age = input("Enter The age: ")  
    
    if not password:
        print("The password is not empty")
        return
        
    if not age.isdigit() or int(age) <= 0:
        print("The Age must be positive integer")
        return
    
    with open(FILE_NAME, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
                if row[0] == username:
                        print("Error: Username already exists. Please try again.")
                        return 
                
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, age, first_name, last_name,"False"])
        print("Signup successful!")


# Function to sign in an existing user
def signin():
    username = input("Enter username: ")
    password = input("Enter password: ")
   
    updated_rows = []
    
    with open(FILE_NAME, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            updated_rows.append(row)
            if row[0] == username and row[1] == password:
                row[5] = "True"
                print("Signin successful!")
                break
            else:
                print("Error: Incorrect username or password. Please try again.")    
            return
            
    with open(FILE_NAME, mode='w', newline='') as file:
         writer = csv.writer(file)
         writer.writerows(updated_rows)
       

# Function to sign out an existing user
def signout():
    username = input("Enter username: ")
    updated_rows = []
    success = False
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            updated_rows.append(row)
            if row[0] == username :
                if row[5] == 'True':
                   row[5] = False
                   print("Logout successful")
                else:
                    print("User is not logged in.")
                break
        else:
            print("username not found")
            return    
    
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)
