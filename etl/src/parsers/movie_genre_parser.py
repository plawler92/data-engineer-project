import ast
import logging

from src.models import Genre

class MovieGenreParser(object):
    def __init__(self, genre_target, join_target):
        self.genre_target = genre_target
        self.join_target = join_target
        self.genres = set()
        self.joins = []

    # Extracts information about genres and separately combines each movie id with 
    # the associated genre id.
    def parse(self, row):
        for genre in ast.literal_eval(row["genres"]):
            genre_id = int(genre["id"])
            self.joins.append({
                "movieid": int(row["id"]),
                "genreid": genre_id
            })
            self.genres.add(Genre(genre_id, genre["name"]))
        # self.records.extend([
        #     {
        #         "movieid": int(row["id"]),
        #         "genre": genre["name"]
        #     }
        #     for genre in ast.literal_eval(row["genres"])
        # ])

    def write(self):
        self.genre_target.write([genre.to_dict() for genre in self.genres])
        self.join_target.write(self.joins)