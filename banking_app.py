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


def user_create():
    create_user_name = input("Enter the new user(eg-U0000): ")
    create_password = input("Enter the new password: ")
    with open("user.txt", "a") as user_data:
        user_data.write(f"{create_user_name} , {create_password}")


    



def admin_create():
    create_admin_name = input("Enter the new user(eg-U0000): ")
    create_password = input("Enter the new password: ")
    with open("user.txt", "a") as user_data:
        user_data.write(f"{create_admin_name} , {create_password}")
    pass




def check_super_admin():

    pass


def check_admin():
    pass


def check_user():
    pass

def get_user_data():
    pass

def get_admin_data():
    pass


















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





def register_user():
    name = input("user name: ")
    address = input("address: ")
    phone_number = input("phone number: ")
    user_ID = U0001

def admin_login():
    while True:
        Admin_name = "A001"
        Password = "A001"
        admin_name = input("Enter the user name")
        password = input("Enter the password")
        if admin_name == Admin_name and password ==Password:
            print("Admin login successful.")
            print("1.Register and create user.")
            print("2.Change password.")
            print("3.deposit.")
            print("4.Withdrow.")
            print("5.Check balance")
            print("6.Transaction History.")
            print("7.Delete user.")
            print("8.Exit.")
            admin_value = int_input()
            if admin_value < 8:
                if admin_value == 1:
                    pass
                elif admin_value == 2:
                    pass
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
                pass
                user_login()
            elif choice == 2:
                pass
                admin_login()

            elif choice == 3:
                pass
                super_admin_login()
        elif choice == 4:
            break
        else:
            print("select correct number.")


