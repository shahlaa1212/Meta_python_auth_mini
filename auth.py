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
    
    with open(FILE_NAME, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
                if row[0] == username:
                        print("Error: Username already exists. Please try again.")
                        return 
                
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, "False"])
        print("Signup successful!")


# Function to sign in an existing user
def signin():
    username = input("Enter username: ")
    password = input("Enter password: ")

    updated_rows = []
    success = False
    
    with open(FILE_NAME, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == username and row[1] == password:
                row[5] = "True"
                success = True
                print("Signin successful!")
            updated_rows.append(row)
        print("Signin failed! Invalid username or password.")    
    
    if success:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(["username", "password"])
            writer.writerows(updated_rows)
        print("Signin successful!")
    else:
        print("Error: Incorrect username or password. Please try again.")


# Function to sign out an existing user
def signout():
    username = input("Enter username: ")
    updated_rows = []
    success = False
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row[0] == username :
                success = True
            updated_rows.append(row)
    
    if success:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])
            writer.writerows(updated_rows)
        print("Signout successful!")
    else:
        print("Error: User is not logged in or does not exist.")