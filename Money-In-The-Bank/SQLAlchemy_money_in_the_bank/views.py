from controllers import ClientAlreadyRegistered, NoSuchCLient
import getpass


class MainView:
    def __init__(self, controller):
        self.controller = controller

    def render(self):
        while True:
            command = input('Enter command>')

            if command == 'register':
                email = input('Email: ')
                name = input('Name: ')
                password = input('Password: ')

                try:
                    self.controller.register(email, name, password)
                    print('You are registered to the system!')
                except ClientAlreadyRegistered as e:
                    print(e)

            elif command == 'login':
                email = input("Email: ")
                password = getpass.getpass("Password:")
                logged_user = self.controller.login(email, password)

                try:
                    self.logged_menu(logged_user)
                    print("You are logged in!")
                except NoSuchCLient as e:
                    print(e)

            elif command == 'help':
                print("login - for logging in!")
                print("register - for creating new account!")
                print("exit - for closing program!")

            elif command == 'exit':
                break
            else:
                print("Not a valid command")

    def logged_menu(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.name)
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.name)
                print("Your email is: " + logged_user.email)
                print("Your balance is:" + str(logged_user.balance) + '$')

            elif command == 'change-pass':
                new_pass = input("Enter your new password: ")
                self.controller.change_password(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                self.controller.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.message)

            elif command == 'help':
                print("info - for showing account info")
                print("change-pass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")
