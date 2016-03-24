import sql_manager
import getpass
from validation import PasswordNotStrongError
import messages


class CLI:

    def __init__(self):
        pass

    def start(self):
        print(messages.WELCOME_MSG)
        while True:
            command = input("$$$>")

            if command == 'register':
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                try:
                    sql_manager.register(username, password)
                    print(messages.SUCCESSFUL_REG_MSG)
                except PasswordNotStrongError:
                    print(messages.STRONG_PASSWORD_ERROR_MSG)

            elif command == 'login':
                username = input("Enter your username: ")
                password = getpass.getpass("Enter your password: ")
                logged_user = sql_manager.login(username, password)

                if logged_user:
                    self.logged_menu(logged_user)
                else:
                    print(messages.LOGIN_FAIL_MSG)

            elif command == 'help':
                print("login - for logging in!")
                print("register - for creating new account!")
                print("exit - for closing program!")

            elif command == 'exit':
                break
            else:
                print("Not a valid command")

    def logged_menu(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'changepass':
                new_pass = input("Enter your new password: ")
                sql_manager.change_pass(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                sql_manager.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")
