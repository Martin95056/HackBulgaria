class UserInterface():

    def __init__(self, controller):
        self.controller = controller
        self.__user_activeness = True
        self._commands = {
            "show_movies": self._show_movies,
            "show_projections": self._show_projections,
            "make_reservation": self._make_reservation,
            "help": self._help,
            "exit": self._exit
        }

    def _show_movies(self, *args):
        print(self.controller.generate_movies_table())

    def _show_projections(self, *args):
        movie_id = args[0]
        date = None
        if len(args) > 1:
            date = args[1]

        print(self.controller.generate_projections_table(movie_id, date))

    def _show_reservations(self, data):
        print(self.controller.generate_reservations_table(data))

    def _exit(self, *args):
        self.__user_activeness = False

    def _help(self, *args):
        print('''Valid commands:
                 show_movies - shows you movies table,
                 show_projections - shows you projections table,
                 make_reservation - to make a reservation,
                 exit''')

    def _make_reservation(self, *args):
        print("Type cancel if you want to abbadon the reservation.")
        while True:
            username = input("Enter your name: ")
            if username is "cancel":
                break
            number_of_tickets = int(input("Enter number of tickets: "))
            if number_of_tickets is "cancel":
                break
            self._show_movies()
            movie_id = int(input("Enter movie id: "))
            if movie_id is "cancel":
                break
            self._show_projections(movie_id)
            projection_id = int(input("Choose projection(by ID!): "))
            if projection_id is "cancel":
                break
            print("Avaliable seats are marked with a dot.\n")

            cinema = self.controller.create_cinema(projection_id)
            self._show_reservations(cinema)
            i = 1
            seats = []
            while i in range(number_of_tickets + 1):
                seat = input("Choose a seat {} row, col: ".format(i)).split(",")
                if seat is "cancel":
                    break
                seat_str = ("({},{})".format(seat[0], seat[1]))
                if cinema[int(seat[0])][int(seat[1])] == 'X':
                    print("Seat is already taken.")
                elif int(seat[0]) > 10 or int(seat[1]) > 10 or int(seat[0]) < 1 or int(seat[1]) < 1:
                    print("We don't have such seat.")
                else:
                    i += 1
                seats.append(seat_str)
            print("YOUR RESERVATION:\n")
            print("Customer \n".format(username))
            print(self.controller.generate_end_of_reservation_table(movie_id, projection_id))
            print("Seats, to be reserved: ")
            for i in seats:
                print(i)

            final = input("Type ok if you are ready with your reservation:")
            if final is "cancel":
                break
            elif final is "ok":
                res_seat = [int(x) for x in seat if x.isdigit() for seat in seats]
                self.controller.reserve_seats(username, projection_id, res_seat[0], res_seat[1])

    def start(self):
        print("Welcome to my cinema :)")
        print("Type help to see the commands")
        while self.__user_activeness:
            command = ""
            parameter1 = None
            parameter2 = None

            user_input = input("Enter command: ").split()
            command = user_input[0]
            if len(user_input) > 1:
                parameter1 = user_input[1]
                if len(user_input) > 2:
                    parameter2 = user_input[2]

            self._commands[command](parameter1, parameter2)
