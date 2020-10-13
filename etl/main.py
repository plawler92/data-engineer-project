import logging

from config import Config
import src.app as app

logging.basicConfig(**Config.logging)

if __name__ == "__main__":
    app.run(Config)