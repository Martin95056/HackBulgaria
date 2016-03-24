import sqlite3

conn = sqlite3.connect('cinema.db')
conn.row_factory = sqlite3.Row
curs = conn.cursor()

create_movies_table = '''CREATE TABLE IF NOT EXISTS Movies
                             (movie_id INTEGER PRIMARY KEY,
                                name TEXT,
                                rating FLOAT)'''
curs.execute(create_movies_table)

create_projections_table = '''CREATE TABLE IF NOT EXISTS Projections
                             (projection_id INTEGER PRIMARY KEY,
                                movie,
                                type VARCHAR(3),
                                date VARCHAR(10),
                                time VARCHAR(5),
                                FOREIGN KEY(movie) REFERENCES Movies(movie_id))
                            '''
curs.execute(create_projections_table)

create_reservations_table = '''CREATE TABLE IF NOT EXISTS Reservations
                             (reservation_id INTEGER PRIMARY KEY,
                                username TEXT,
                                projection_id,
                                row TINYINT,
                                col TINYINT,
                                FOREIGN KEY(projection_id)
                                REFERENCES Projections(projection_id))
                             '''
curs.execute(create_reservations_table)

conn.commit()

insert_into_movies = '''INSERT INTO Movies (movie_id, name, rating)
                             VALUES
                             (1, "The Hunger Games", 7.9),
                             (2, "Wreck-It Ralph", 7.8),
                             (3, "Her", 8.3)
                            '''
curs.execute(insert_into_movies)

insert_into_projections = '''INSERT INTO Projections (projection_id, movie, type, date, time)
                             VALUES
                             (1,1, "3D", "2014-04-01", "19:10"),
                             (2,1, "2D", "2014-04-01", "19:00"),
                             (3,1, "4DX", "2014-04-02", "21:00"),
                             (4,3, "2D", "2014-04-05", "20:20"),
                             (5,2, "3D", "2014-04-02", "22:00"),
                             (6,2, "2D", "2014-04-02", "19:30")
                            '''
curs.execute(insert_into_projections)

insert_into_reservations = '''INSERT INTO Reservations (username, projection_id, row, col)
                             VALUES
                             ("RadoRado", 1, 2, 1),
                             ("RadoRado", 1, 3, 5),
                             ("RadoRado", 1, 7, 8),
                             ("Ivo", 3, 1, 1),
                             ("Ivo", 3, 1, 2),
                             ("Mysterious", 5, 2, 3),
                             ("Mysterious", 5, 2, 4)
                            '''
curs.execute(insert_into_reservations)

conn.commit()
