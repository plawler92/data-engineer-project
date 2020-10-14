class Genre(object):
    # Used by a set to allow only one instance per id
    def __init__(self, genre_id, genre):
        self.genre_id = genre_id
        self.genre = genre

    def to_dict(self):
        return {
            "genreid": self.genre_id,
            "genre": self.genre
        }

    def __eq__(self, other):
        return isinstance(other, Genre) and self.genre_id == other.genre_id

    def __hash__(self):
        return hash(self.genre_id)