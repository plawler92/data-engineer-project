import pytest 

from src.parsers import MovieGenreParser
from tests.dummy_target import DummyTarget

def test_movie_genre_parse_succeeds():
    movie_id = 1
    genre = "Comedy"

    movies = [
        create_movie_genre_str(movie_id, genre)
    ]

    dummy_target = DummyTarget()
    movie_genre_parser = MovieGenreParser(dummy_target)

    for movie in movies:
        movie_genre_parser.parse(movie)
    movie_genre_parser.write()

    result = dummy_target.items[0]

    assert result["movieid"] == movie_id
    assert result["genre"] == genre

def create_movie_genre_str(movie_id, genre):
    return {
        'id': str(movie_id),
        'genres': "[{'id': '1000', 'name': '" + genre + "'}]"
    }