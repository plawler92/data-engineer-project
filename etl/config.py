import os
import logging

class Config(object):
    sources = {
        "movies": "../data/small_clean_movies.csv"
    }
    targets = {
        "movies": "output/movie.json",
        "movie_genres": "output/movie_genres.json",
        "production_companies": "output/production_companies.json",
        "movie_company_join": "output/movie_company_join.json"
    }
    logging = {
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "level": logging.INFO
    }