from data_communicator import DataCommunicator
from controler import Controller
from interface import UserInterface
import sqlite3


def main():
    conn = sqlite3.connect('cinema.db')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    db_communicator = DataCommunicator(curs)
    controller = Controller(db_communicator)
    cli = UserInterface(controller)
    cli.start()


if __name__ == '__main__':
    main()
