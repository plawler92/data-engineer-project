import pytest 

from src.parsers import MovieGenreParser
from tests.dummy_target import DummyTarget

def test_movie_genre_parse_succeeds():
    movie_id = 1
    genre_id = 17
    genre = "Comedy"

    movie = create_movie_genre_str(movie_id, genre_id, genre)

    dummy_genre_target = DummyTarget()
    dummy_join_target = DummyTarget()
    movie_genre_parser = MovieGenreParser(dummy_genre_target, dummy_join_target)

    movie_genre_parser.parse(movie)
    movie_genre_parser.write()

    genre_result = dummy_genre_target.items[0]
    join_result = dummy_join_target.items[0]


    assert genre_result["genreid"] == genre_id
    assert genre_result["genre"] == genre
    assert join_result["movieid"] == movie_id
    assert join_result["genreid"] == genre_id

def create_movie_genre_str(movie_id, genre_id, genre):
    return {
        'id': str(movie_id),
        'genres': "[{'id': '" + str(genre_id) + "', 'name': '" + genre + "'}]"
    }