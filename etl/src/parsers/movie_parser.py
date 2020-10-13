from decimal import Decimal

class MovieParser(object):
    def __init__(self, movie_target):
        self.movie_target = movie_target
        self.movies = []
    
    # extracts data about a movie. calculates profit = revenue - budget.
    def parse(self, row):
        revenue = int(row["revenue"])
        budget = int(row["budget"])
        self.movies.append({
            "movieid": int(row["id"]),
            "budget": budget,
            "popularity": float(row["popularity"]),
            "revenue": revenue,
            "profit": revenue - budget,
            "releasedate": row["release_date"]
        })

    def write(self):
        self.movie_target.write(self.movies)