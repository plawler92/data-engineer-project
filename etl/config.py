import os
import logging

class Config(object):
    sources = {
        "movies": "../data/movies_metadata.csv"
    }
    targets = {
        "movies": "output/movie.json",
        "genres": "output/genres.json",
        "movie_genre_join": "output/movie_genre_join.json",
        "production_companies": "output/production_companies.json",
        "movie_company_join": "output/movie_company_join.json",
    }
    logging = {
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "level": logging.INFO
    }