# python banking_app.py

def int_input():
    while True:
        try:
            int_number = int(input("Enter your choice: "))
            if int_number > 0:
                return int_number
                break
            else:
                print("Enter your positive number.")               
        except ValueError:
            print("Enter your integer value.")

def withdraw_money():
    while True:
        withdrow_amount = int_input()
        balance = 100000
        if withdrow_amount <= balance:
            balance -= withdrow_amount
            print("new balance is: ", balance)
            break
        else:
            print("Enter the correct value.")

def deposit_money():
    while True:
        deposit_amount = int_input()
        balance = 100000
        balance += deposit_amount
        print("new balance after deposit: ", balance)
        break

def register_user():
    name = input("user name: ")
    address = input("address: ")
    phone_number = input("phone number: ")
    user_name = input("create user name: ")
    password = input("create user password: ")
    try:
        create_user_ID = open("registration.txt", "r")
        user_ID_list = []
        user_ID_list = create_user_ID.readlines()
        create_user_ID.close()
    except FileNotFoundError:
        user_ID_list = []
    if len(user_ID_list) == 0:
        user_ID = f"U1001"
    else:
        last_line = user_ID_list[-1].strip()
        z = int(last_line.split(",")[0].strip()[1:]) + 1
        user_ID = f"U{z}"

    with open("registration.txt", "a") as registration:
        registration.write(f"{user_ID}, name: {name}, address: {address}, phone number: {phone_number}\n")

    with open('user.txt', 'a') as user_login:
        user_login.write(f"{user_ID}, user name: {user_name}, password: {password}")

def register_admin():
    name = input("admin name: ")
    address = input("address: ")
    phone_number = input("phone number: ")
    admin_name = input("create admin name: ")
    password = input("create admin password: ")
    try:
        create_admin_ID = open("admin_registration.txt", "r")
        admin_ID_list = []
        admin_ID_list = create_admin_ID.readlines()
        create_admin_ID.close()
    except FileNotFoundError:
        admin_ID_list = []

    if len(admin_ID_list) == 0:
        admin_ID = f"U1001"
    else:
        last_line = admin_ID_list[-1].strip()
        z = int(last_line.split(",")[0].strip()[1:]) + 1
        admin_ID = f"A{z}"

    with open("admin_registration.txt", "a") as registration:
        registration.write(f"{admin_ID}, name: {name}, address: {address}, phone number: {phone_number}\n")

    with open('admin.txt', 'a') as user_login:
        user_login.write(f"{admin_ID}, user name: {admin_name}, password: {password}")

def user_login():
    while True:
        User_name = "U001"
        Password = "U001"
        user_name = input("Enter the user name")
        password = input("Enter the password")
        check_user = check_user()
        if user_name == User_name and password ==Password:
            print("User login successful.")
            print("1.Deposit.")
            print("2.Withdraw.")
            print("3.Check balance")
            print("4.Transaction History.")
            print("5.Exit")
            value = int_input()
            if value < 5:
                if value == 1:
                    pass
                elif value == 2:
                    pass
                elif value == 3:
                    pass
                elif value == 4:
                    pass
            elif value == 5:
                break
            else:
                print("value select correct number")

            
        else:
            print("Invalid user name or password")

def change_user_name_password():
    with open('user.txt', 'r') as change:
        user_ID = input("Enter the user ID: ")
        x = []
        a = {}
        x = change.readlines()
        for i in x:
            y = i.strip()
            z = y.split(",")[0].strip()
            a[z] =  [y.split(",")[1].strip()[6:],  y.split(",")[2].strip()[10:]]

            if user_ID == z:
                new_username = input("Enter the new user name: ")
                new_password = input("Enter the new password: ")
                a[user_ID] =[new_username,new_password]
                b = 0
            for key,values in a.items():
                if b == 0:
                    with open('user.txt', 'w') as update:
                        update.write(f"{key}, user name: {values[0]}, password: {values[1]}\n")
                        b = 1
                else:
                    with open('user.txt', 'a') as update:
                        update.write(f"{key}, user name: {values[0]}, password: {values[1]}\n")

            print("finished user update...")

def change_admin_name_password():
    with open('admin.txt', 'r') as change:
        admin_ID = input("Enter the user ID: ")
        x = []
        a = {}
        x = change.readlines()
        for i in x:
            y = i.strip()
            z = y.split(",")[0].strip()
            a[z] =  [y.split(",")[1].strip()[6:],  y.split(",")[2].strip()[10:]]

            if admin_ID == z:
                new_admin_name = input("Enter the new admin name: ")
                new_password = input("Enter the new password: ")
                a[admin_ID] =[new_admin_name,new_password]
            b = 0
            for key,values in a.items():
                if b == 0:
                    with open('admin.txt', 'w') as update:
                        update.write(f"{key}, user name: {values[0]}, password: {values[1]}\n")
                    b = 1
                else:
                    with open('admin.txt', 'a') as update:
                        update.write(f"{key}, user name: {values[0]}, password: {values[1]}\n")
            print("finished admin update...")

def admin_login():
    while True:
        with open('admin.txt','r') as check_admin:
            pass
            # check_admin_list = che
        Admin_name = "A001"
        Password = "A001"
        admin_name = input("Enter the user name")
        password = input("Enter the password")
        if admin_name == Admin_name and password ==Password:
            print("Admin login successful.")
            print("1.Register and create user.")
            print("2.Change user name and password.")
            print("3.deposit.")
            print("4.Withdrow.")
            print("5.Check balance")
            print("6.Transaction History.")
            print("7.Delete user.")
            print("8.Exit.")
            admin_value = int_input()
            if admin_value < 8:
                if admin_value == 1:
                    register_user()
                elif admin_value == 2:
                    change_user_name_password()
                elif admin_value == 3:
                    pass
                elif admin_value == 4:
                    pass
                elif admin_value == 5:
                    pass
                elif admin_value == 6:
                    pass
                elif admin_value == 7:
                    pass
            elif admin_value == 8:
                break
            else:
                print("value select correct number")

        else:
            print("Invalid user name or password")

def super_admin_login():
    while True:
        Super_admin_name = "S001"
        Password = "S001"
        super_admin_name = input("Enter the user name")
        password = input("Enter the password")
        if Super_admin_name == super_admin_name and password ==Password:
            print("Super admin login successful.")
            print("1.register admin.")
            print("2.Change admin name and password.")
            print("3.Change user name and password.")
            print("Super admin login successful.")
            choice = int_input()
            if choice == 1:
                register_admin()
            elif choice == 2:
                change_admin_name_password()
            elif choice == 3:
                change_user_name_password()
            else:
                print("Enter the correct value")
            break
        else:
            print("Invalid user name or password")

def Main():
    while True:
        print("-----mini banking app-----")
        print("1.User login.")
        print("2.Admin login.")
        print("3.super admin login.")
        print("4.Exit.")
        choice = int_input()
        if choice < 4:
            if choice == 1:
                user_login()
            elif choice == 2:
                admin_login()
            elif choice == 3:
                super_admin_login()
        elif choice == 4:
            break
        else:
            print("select correct number.")
