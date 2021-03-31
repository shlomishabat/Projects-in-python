import mysql.connector
# Instructions
# 1. Make sure you have a server and make sure it is turned on
# (You can use any server software you want for example: "xampp"
# 2.Replace the host address and username in the first two functions (if you also have a password you can add it there)
# 3. *******DO NOT CHANGE THE NAME OF THE DATABASE ******(the software creates everything for you :))
# if you wont to expand all press ctrl+shift+ NUMPAD+


def create_server_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # change here the host if necessary
            user="root",  # change here the user if necessary
        )
        return connection
    except:
        return "Error"


def create_database_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # change here the host if necessary
            user="root",  # change here the user if necessary
            database="atmdatabase",  # DO NOT CHANGE  OF THE DATABASE !!!!
        )
        return connection
    except:
        create_database()


def create_database():
    try:
        atmdatabase = create_server_connection()
        mycursor = atmdatabase.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS `atmdatabase`"
        mycursor.execute(sql)
        atmdatabase.commit()
        create_table()
    except ValueError:
        print("connection error")


def create_table():
    atmdatabase = create_database_connection()
    mycursor = atmdatabase.cursor()
    sql = "CREATE TABLE IF NOT EXISTS `atmdatabase`.`users` " \
          "( `id` INT(11) NOT NULL AUTO_INCREMENT, PRIMARY KEY (`id`)" \
          " , `name` VARCHAR(300) NOT NULL , `" \
         "password` INT(4) NOT NULL , `balance` INT(11) NOT NULL ) ENGINE = InnoDB;"
    mycursor.execute(sql)
    atmdatabase.commit()


def isvalid(user_name, user_password):
    atmdatabase = create_database_connection()
    mycursor = atmdatabase.cursor()
    sql = "SELECT * FROM `users` WHERE `name` = '" + str(user_name) + "' AND password ='" + str(user_password) + "'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for row in result:
        return row
    else:
        return "worng"


def update_user(id, user_name, user_password, user_balance):
    atmdatabase = create_database_connection()
    mycursor = atmdatabase.cursor()
    sql = "UPDATE `users` SET `id`='" + str(id) + "',`name`='" + user_name + \
          "',`password`='" + str(user_password) + "',`balance`='" + str(user_balance) + "' WHERE `id`= '" + str(id) + "'"
    mycursor.execute(sql)
    atmdatabase.commit()


def new_user(user_name, user_password, balance):
    atmdatabase = create_database_connection()
    mycursor = atmdatabase.cursor()
    sql = "INSERT INTO `users` (`id`, `name`, `password`, `balance`)" \
          " VALUES (NULL,'" + user_name + "','" + str(user_password) + "','" + str(balance) + "') "
    mycursor.execute(sql)
    atmdatabase.commit()


def select_user(user_name, user_password):
    atmdatabase = create_database_connection()
    mycursor = atmdatabase.cursor()
    sql = "SELECT * FROM `users` WHERE `name`='" + str(user_name) + "' AND `password`='" + str(user_password) + "'"
    mycursor.execute(sql)
    user_line = mycursor.fetchall()
    for row in user_line:
        return row
    return ""


def money_validate(amount):
    if ((int(amount) / 20) % 2.5) == 0:
        return True
    else:
        return False


def money_switcher(num):
    switcher = {
        1: 50,
        2: 100,
        3: 150,
        4: 300,
    }
    return switcher.get(num, num)
#  ********************* MAIN CLASS *************************


create_database()
create_table()
count = 3
while create_server_connection() != "Error":
    if count <= 0:
        print("YOU ARE BLOCKED BY THE ADMIN")
        exit()
    user = str(input("Welcome to PYTHON ATM console application\n"
                     "*****************************************\n"
                     "for new user type 'new'(small letters) \n "
                     "for Exists user type your user name\n>>>>>>"))
    while user == "new":
            name = str(input("please insert your name> "))
            password = int(input("please insert new password> "))
            balance = int(input("please insert your balance> "))
            if (len(str(password)) == 4) & money_validate(balance):
                if select_user(name, password) == "":
                    new_user(name, password, balance)
                    user = str(input("your user create successfully! \n please insert your name for log in \n >>>>>> "))
                else:
                    user = str(input("The user already exists! \n If you still want to create a new user type 'NEW' \n"
                                     " if you want to login type your username \n >>>>>> "))

            else:
                print("Sorry, your password should be 4 digits long,\n"
                      " and your initial deposit amount should be divided by 20 50 100 bills\n TRY AGAIN !.")
    else:
        password = int(input("please insert your password> "))
        row = isvalid(user, password)
        row_id = row[0]
        row_name = row[1]
        row_password = row[2]
        row_balance = row[3]
        if row_password == password:
            count = 3
            choice = "null"
            while choice != "q":
                choice = input("*****ATM MENU***** \n"
                               " Press d to Deposit Money\n"
                               " Press w to Withdraw Money \n"
                               " Press c to Check your Balance \n"
                               " Press p to change your password \n "
                               " Press q to Quit\n"
                               " >>>>> ")
                if choice == "d":
                    deposit = int(input("How much would you like to Deposit?> "))
                    if money_validate(deposit):
                        row_balance += deposit
                        update_user(row_id, row_name, row_password, row_balance)
                        print("Successful,Your current Balance is: " + str(row_balance))
                    else:
                        print("Sorry, you can deposit only multiplier of 20 50 100 bill")
                elif choice == "w":
                    withdraw = int(input("How much would you like to withdraw?\n"
                                         "  1 for 50₪\n"
                                         " 2 for 100₪\n"
                                         " 3 for 150₪\n"
                                         " 4 for 300₪\n"
                                         " 5 for other\n"
                                         ">>>>"))
                    if withdraw == 5:
                        withdraw = int(input("please insert the amount> "))
                    if money_validate(money_switcher(withdraw)):
                        if withdraw <= row_balance:
                            row_balance -= money_switcher(withdraw)
                            update_user(row_id, row_name, row_password, row_balance)
                            print("Successful,Your current Balance is: " + str(row_balance))
                        else:
                            print("sorry, operation could happen, insefitioned amount /"
                                  " you don't have enough Balace for this operaion")

                elif choice == "p":
                    passValid = int(input("please insert your old password\n>>>>"))
                    if row_password == passValid:
                        newPass = int(input("please insert your new password\n>>>>"))
                        newPassValid = int(input("please insert your new password again\n>>>>"))
                        if newPass == newPassValid:
                            update_user(row_id, row_name, newPass, row_balance)
                            print("Your password has been successfully changed")
                elif choice == "c":
                    print("Your current Balance is: " + str(row_balance))
                if choice == "q":
                    print("GOOD BAY, HAVE A NICE DAY\n"
                        "****************************")
        else:
            count -= 1
            print("wrong details,You have "+str(count)+" attempts left ")
else:
    print("Server connection Error ")
