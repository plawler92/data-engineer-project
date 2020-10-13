import ast

class MovieGenreParser(object):
    def __init__(self, movie_genre_target):
        self.movie_genre_target = movie_genre_target
        self.records = []

    # extracts a row combining movie id with each associated genre
    def parse(self, row):
        self.records.extend([
            {
                "movieid": int(row["id"]),
                "genre": genre["name"]
            }
            for genre in ast.literal_eval(row["genres"])
        ])

    def write(self):
        self.movie_genre_target.write(self.records)