import sys
import csv
import string
import os


# curr_user = ""
# users = ["eq"]
# passwords = ["t"]
username = ""
first_login = True
file_user = open("./users.csv", "a")
file_pass = open("./passwords.csv", "a")
# file_user.write("TestUser")
# file_pass.write("TestPass")
file_user.close()
file_pass.close()


# WELCOME MESSAGE
msg = """
Welcome to my playground!
Please enter your username and password to continue.
"""

print(msg)


# MAIN MENU MESSAGE
menu_msg = """
Please type in one of the below Options:
M - Main Menu
F - Find User
C - Calculator
P - Password Menu
Q - Quit
"""

# CALC MENU MESSAGE
calc_msg = f"""
Welcome to Calculator Menu {username}!

Please type in one of the below Options:
A - Add
S - Subtract
M - Multiply
D - Divide
Q - Go Back to Main Menu
"""


# CALCULATOR FUNCTIONS
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


# CONTINUE OPTION
def conti():
    cont_conf = input("Would you like to continue? Y/N ")
    if cont_conf.upper() == "Y":
        return calc_menu()
    elif cont_conf.upper() == "N":
        return menu()
    else:
        print("Invalid Option")
        return conti()


# CALCULATOR MENU
def calc_menu():
    print(f"""
Welcome to Calculator Menu {username}!

Please type in one of the below Options:
    A - Add
    S - Subtract
    M - Multiply
    D - Divide
    B - Back to Main Menu
    """)

    answer_calc = input(f"Okay {username}!\nWhat would you like to calculate? ")

    if answer_calc.upper() == "A":
        n1 = float(input("Please enter the first number: "))
        n2 = float(input("Please enter the second number: "))
        print(n1, "+", n2, "=", add(n1, n2))
        return conti()

    elif answer_calc.upper() == "S":
        n1 = float(input("Please enter the first number: "))
        n2 = float(input("Please enter the second number: "))
        print(n1, "-", n2, "=", subtract(n1, n2))
        return conti()

    elif answer_calc.upper() == "M":
        n1 = float(input("Please enter the first number: "))
        n2 = float(input("Please enter the second number: "))
        print(n1, "*", n2, "=", multiply(n1, n2))
        return conti()

    elif answer_calc.upper() == "D":
        n1 = float(input("Please enter the first number: "))
        n2 = float(input("Please enter the second number: "))
        print(n1, "/", n2, "=", divide(n1, n2))
        return conti()

    elif answer_calc.upper() == "B":
        return menu()

    else:
        print("Incorrect command.")
        return menu()


# CHANGE PASSWORD/USER MENU
def change_pass(find_u):
    print(f"""Welcome to User Menu {username}!

Please type in one of the below Options:
    P - Change Password for {find_u}
    M - Main Menu
    U - User Directory
    D - Delete {find_u} User
    F - Find another User
""")
    answer_one = input("What would you like to do now? ")
    if answer_one.upper() == "M":
        menu()
    elif answer_one.upper() == "P":
        print("Change Password")
        passw = input("Please enter your current Password: ")
        passw_v = input("Please enter your new Password: ")
        passw_vtwo = input("Please re-enter your new Password: ")
        if username in open("users.csv").read() and passw in open("passwords.csv").read():
            print("Verification Complete")
            if passw_v.upper() == passw_vtwo.upper():
                file_pass = open("./passwords.csv", "w")
                file_pass.write(passw_vtwo + ",\n")
                file_pass.close()
                print(f"Password for {username} successfully changed!\nYou can now login.")
                sys.exit()
            else:
                print("Passwords do not match!")
                return change_pass(find_u)
    elif answer_one.upper() == "D":
        print(f"Delete {find_u}")
        delete_user(find_u)
    elif answer_one.upper() == "F":
        find_user()
    elif answer_one.upper() == "U":
        with open("users.csv") as csvfile:
            read_obj = csv.reader(csvfile, delimiter=',')
            for value in read_obj:
                if len(value) < 5:
                    print(value[:-1])
            else:
                change_pass(find_u)


# FIND USER MENU
def find_user():
    find_u = input("What user would you like to find? ")
    if find_u.upper() == "Q" or find_u.upper() == "M":
        return menu()
    elif find_u in open('users.csv').read():
        print(f"{find_u} has been found.")
        return change_pass(find_u)
    else:
        print(f"{find_u} does not exist!\nType Q or M to go back.")
        return find_user()


# MAIN MENU FUNCTION
def menu():

    print(menu_msg)
    answer = input(f"Okay {username}!\nWhat would you like to try out? ")

    if answer.upper() == "M":
        return menu()

    elif answer.upper() == "F":
        return find_user()

    elif answer.upper() == "C":
        return calc_menu()

    elif answer.upper() == "P":
        return change_pass(username)

    elif answer.upper() == "Q":
        print(f"You have successfully logged out.\nHave a nice day {username}!")
        return sys.exit()

    else:
        print("Incorrect command.")
        return menu()


# PASSWORD/USER VERIFICATION
def login():
    pass_attempt = 0
    while pass_attempt < 3:
        pwd = input("What is your Password? ")
        if username in open("users.csv").read() and pwd in open("passwords.csv").read():
            print("Verification Complete")
            return menu()
        else:
            print("Something isn't right!")
            pass_attempt += 1
    else:
        print("Too many failed attempts!")
        return sys.exit()


# CREATE USER
def create_user():
    # users.append(username)
    passw = input("Please chose a secure Password: ")
    passw_v = input("Please re-enter your Password: ")
    if passw.upper() == passw_v.upper():
        file_user = open("./users.csv", "a")
        file_pass = open("./passwords.csv", "a")
        file_user.write(username + ",\n")
        file_pass.write(passw_v + ",\n")
        file_user.close()
        file_pass.close()
        print(f"Account {username} successfully created!\nYou can now login.")
        return sys.exit()
    else:
        print("Passwords do not match!")
        return menu()

# DELETE USER
def delete_user(find_u):
    # users.append(username)
    passw = input(f"Please enter Password to delete {find_u}: ")
    passw_v = input(f"Please re-enter Password to delete {find_u}: ")
    if passw.upper() == passw_v.upper():
        file_user = open("./users.csv", "w")
        file_pass = open("./passwords.csv", "w")
        file_user.write("")
        file_pass.write("")
        file_user.close()
        file_pass.close()
        print(f"Account {find_u} successfully removed!\nPlease login to continue.")
        return sys.exit()
    else:
        print("Passwords do not match!")
        return menu()


# CHECK IF USER EXISTS
while first_login:
    exists_in_file = False
    username = input("What is your Username? ")
    if len(username) < 5:
        print("Username too Short!")
    else:
        with open("users.csv", "r+") as csvfile:
            my_content = csv.reader(csvfile, delimiter=',')
            for row in my_content:
                if username in row:
                    is_in_file = True
                    first_login = False
                    login()
            else:
                answer = input(f"Would you like to create user {username}? Y/N ")
                if answer.upper() == "Y":
                    create_user()
                elif answer.upper() == "N":
                    first_login = True
                    continue
                else:
                    print("Invalid Option")
                    menu()