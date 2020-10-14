import logging
import time

from src.sources import LocalCSVSource
from src.targets import LocalJSONTarget
from src.parsers import MovieGenreParser, ProductionCompanyParser, MovieParser
from src.transformers import MovieTransformer

logger = logging.getLogger(__name__)

def run(config):
    # Initializes objects that handle trasnforming source data and loading the result to targets
    movie_source = LocalCSVSource(config.sources["movies"])

    movie_target = LocalJSONTarget(config.targets["movies"])
    genre_target = LocalJSONTarget(config.targets["genres"])
    movie_genre_target = LocalJSONTarget(config.targets["movie_genre_join"])
    company_target = LocalJSONTarget(config.targets["production_companies"])
    movie_company_target = LocalJSONTarget(config.targets["movie_company_join"])

    movie_parser = MovieParser(movie_target)
    movie_genre_parser = MovieGenreParser(genre_target, movie_genre_target)
    company_parser = ProductionCompanyParser(company_target, movie_company_target)

    movie_transformer = MovieTransformer(movie_source, [movie_parser, movie_genre_parser, company_parser])

    try:
        logger.info("Starting Transformations...")
        start_transform = time.time()
        movie_transformer.transform()

        start_write = time.time()
        logger.info(f"Transformations complete after {start_write - start_transform:,.3f} seconds...")
        logger.info(f"Starting load...")
        movie_transformer.write()

        end = time.time()
        logger.info(f"Load complete after {end - start_write:,.3f} seconds")
    except Exception as e:
        logger.error(str(e))
        #raise e