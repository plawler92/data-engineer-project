import pytest

from src.parsers import MovieParser
from tests.dummy_target import DummyTarget

def test_movie_parse_succeeds():
    movie_id = 1
    budget = 100
    revenue = 200
    popularity = 300.12345
    release_date = "2019-01-01"
    
    movies = [
        create_movie_str(movie_id, budget, popularity, revenue, release_date)
    ]

    dummy_target = DummyTarget()
    movie_parser = MovieParser(dummy_target)

    for movie in movies:
        movie_parser.parse(movie)
    movie_parser.write()

    result = dummy_target.items[0]

    assert result["movieid"] == movie_id
    assert result["budget"] == budget
    assert result["popularity"] == popularity
    assert result["revenue"] == revenue
    assert result["profit"] == revenue - budget
    assert result["releasedate"] == release_date

def create_movie_str(movie_id, budget, popularity, revenue, release_date):
    return {
        "id": str(movie_id),
        "budget": str(budget),
        "popularity": str(popularity),
        "revenue": str(revenue),
        "release_date": str(release_date)
    }