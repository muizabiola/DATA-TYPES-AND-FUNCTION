# 1. Write a Python program that creates a text file called "student.txt" 
#    and writes the names of 5 students into it. Then read and print the content.
# file_name = "student.txt"
# students = ["Alice", "Bob", "Charlie", "David", "Eva"]
# with open(file_name, 'w') as file:
#     for student in students:
#         file.write(student + "\n")
# with open(file_name, 'r') as file:
#     content = file.read()
#     print(content)


file=open("student.txt", "w")
file.write("alice\n")
file.write("bob\n")
file.write("charlie\n")
file.write("david\n")
file.write("eva\n")
file.close()

file=open("student.txt", "r")
content=file.read()
print(content)
file.close()
    

# 2. Write a Python program to read numbers from a file called "numbers.txt" 
#    and print their sum. Handle the case where the file does not exist.
file = open("numbers.txt", "w")
file.write("ade is a boy")
file.close()

file = open("numbers.txt", "r")
print(file.read())
file.close()




# 3. Write a Python program that asks the user to input text and saves it to a file "notes.txt". 
#    Then reopen the file and display its contents.

user_input = input("Enter some text: ")
with open("notes.txt", "w") as file:
    file.write(user_input)
with open("notes.txt", "r") as file:
    content = file.read()
    print("Content of notes.txt:")
    print(content)


# 4. Write a program that appends the current date and time to a file "log.txt" 
#    every time the program is run.
from datetime import datetime
with open("log.txt", "a") as file:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"Program run at: {current_time}\n")
    file.close()


# 5. Create a program that reads a file called "data.txt" line by line 
#    and counts how many lines, words, and characters it contains. 
#    Handle exceptions if the file is missing.

try:
    with open("data.txt", "w") as file:
        file.write("Hello world\n")
        file.write("This is a sample file.\n")
        file.write("It contains multiple lines of text.\n")
        file.write("Each line has several words.\n")
        file.write("This is the last line.\n")

    with open("data.txt", "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")
except FileNotFoundError:
    print("The file 'data.txt' does not exist.")
finally:
    print("File operation completed.")
    


# 6. Write a Python program that asks the user for a number and divides 100 by that number. 
#    Handle ZeroDivisionError and ValueError exceptions properly.
try:
    number = int(input("Enter a number to divide 100 by: "))
    result = 100 / number
    print(f"100 divided by {number} is {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid integer.")
finally:
    print("Operation completed.")

# 7. Create a program that tries to open "config.json". 
#    If the file does not exist, create it with default settings (use JSON format).
import json
default_settings = {
    "setting1": True,
    "setting2": "default_value",
    "setting3": 10
}
try:
    with open("config.json", "r") as file:
        config = json.load(file)
        print("Config loaded:", config)
except FileNotFoundError:
    with open("config.json", "w") as file:
        json.dump(default_settings, file, indent=4)
        print("Config file created with default settings.")
finally:
    print("File operation completed.")





# 8. Write a program to copy the contents of "source.txt" into another file "destination.txt". 
#    Handle exceptions if the source file is missing.
try:
    with open("source.txt", "w") as source_file:
        source_file.write("This is a sample text file.")
    with open("source.txt", "r") as source_file:
        content = source_file.read()
    with open("destination.txt", "w") as dest_file:
        dest_file.write(content)
    print("File copied successfully.")
except FileNotFoundError:
    print("Error: 'source.txt' does not exist.")
finally:
    print("File operation completed.")
    

# 9. Write a program that takes a filename from the user and tries to open it. 
#    If the file does not exist, print "File not found". 
#    If it exists, display its content.
filename = input("Enter the filename to open: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("File not found.")
finally:
        print("File operation completed.")




# 10. Write a Python program that simulates a simple login system: 
#     - Store usernames and passwords in a file "users.txt" 
#     - Ask the user for username and password 
#     - Check if the credentials exist in the file 
#     Handle FileNotFoundError if "users.txt" does not exist.
import os
users_file = "users.txt"
if not os.path.exists(users_file):
    with open(users_file, "w") as file:
        file.write("user1,password1\n")
        file.write("user2,password2\n")
        file.write("user3,password3\n")
try:
    usernames = input("Enter username: ")
    passwords = input("Enter password: ")
    with open(users_file, "r") as file:
        users = file.readlines()
        credentials = [line.strip().split(",") for line in users]
        if [username, password] in credentials:
    
    
        else:
            print("Invalid username or password.")
except FileNotFoundError:
    print("Error: 'users.txt' does not exist.")
finally:
    print("Login attempt completed.")

