from prettytable import PrettyTable
import settings
import sqlite3


class Controller:

    def __init__(self, db_conn):
        self.db_conn = db_conn

    def generate_movies_table(self):
        table = PrettyTable(['ID', 'Movie', 'Rating'])
        for movie in self.db_conn._get_movies():
            table.add_row([movie['movie_id'], movie['name'], movie['rating']])

        return str(table)

    def create_cinema(self, projection_id):
        rows = settings.ROWS
        cols = settings.COLS
        db_data = self.db_conn._get_reservations(projection_id)
        cinema = []

        row_headers = [" " if x == 0 else x for x in range(rows + 1)]
        cinema.append(row_headers)

        for row in range(rows):
            cinema.append([str(row + 1) if col == 0
                           else "." for col in range(cols+1)])

        for row in db_data:
            cinema[row["row"]][row["col"]] = "X"

        return cinema

    def generate_projections_table(self, movie_id, date):
        if date is not None:
            db_result = self.db_conn._get_movie_projections_with_date(movie_id, date)
        else:
            db_result = self.db_conn._get_movie_projections(movie_id)

        table = PrettyTable(['ID', 'Type', 'Date', 'Time'])

        for projection in db_result:
            table.add_row([projection['projection_id'], projection['type'],
                           projection['date'], projection['time']])

        return str(table)

    def generate_end_of_reservation_table(self, movie_id, proj_id):
        table = PrettyTable(['Movie', 'Type', 'Date', 'Time'])
        db_data = self.db_conn._get_movie_for_specific_projection(movie_id, proj_id)
        for row in db_data:
            table.add_row([row["name"], row["type"], row["date"], row["time"]])

        return str(table)

    def generate_reservations_table(self, data):
        table = PrettyTable(data[0])
        for row in data[1:]:
            table.add_row(row)

        return str(table)

    def reserve_seats(self, username, proj_id, row, col):
        self.db_conn.insert_submitted_reservations(username, proj_id, row, col)
        self.db_conn.commit()
