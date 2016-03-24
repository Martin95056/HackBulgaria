class DataCommunicator():

    def __init__(self, cursor):
        self.cursor = cursor

    def _get_movies(self):
        return self.cursor.execute('''SELECT movie_id, name, rating
                                    FROM Movies
                                    ORDER BY rating DESC
                                    ''')

    def _get_movie_projections(self, id):
        return self.cursor.execute('''SELECT p.projection_id, p.type, p.date, p.time,
                                                  m.movie_id, m.name
                                            FROM Projections as p
                                            JOIN Movies as m
                                            ON m.movie_id = p.movie
                                            WHERE m.movie_id=?
                                            ORDER BY p.date
                                            ''', (id,))

    def _get_movie_projections_with_date(self, id, date):
        return self.cursor.execute('''SELECT p.projection_id, p.type, p.date, p.time,
                                                  m.movie_id, m.name
                                            FROM Projections as p
                                            JOIN Movies as m
                                            ON m.movie_id = p.movie
                                            WHERE m.movie_id=?
                                            AND p.date=?
                                            ORDER BY p.date
                                            ''', (id, date))

    def _get_movie_for_specific_projection(self, movie_id, proj_id):
        return self.cursor.execute('''SELECT p.type, p.date, p.time, m.name
                                            FROM Projections as p
                                            JOIN Movies as m
                                            ON m.movie_id = p.movie
                                            WHERE m.movie_id=?
                                            AND p.projection_id=?
                                            ''', (movie_id, proj_id))

    def _get_reservations(self, projection_id):
        return self.cursor.execute('''SELECT row, col
                                      FROM Reservations
                                      WHERE projection_id=?
                                     ''', (projection_id,))

    def insert_submitted_reservations(self, username, proj_id, row, col):
        return self.cursor.execute('''INSERT INTO Reservations (username, projection_id, row, col)
                                     VALUES
                                     (?, ?, ?, ?)
                                    ''', (username, proj_id, row, col))
