import logging

logger = logging.getLogger(__name__)

class MovieTransformer(object):
    def __init__(self, source, parsers):
        self.source = source
        self.parsers = parsers

    # Reads from source and send the row through each parsers
    # applied to this transformer
    def transform(self):
        for row in self.source.read():
            try:
                for parser in self.parsers:
                    parser.parse(row)
            except Exception as e:
                logger.error(f"Error parsing row `{row}` with {str(e)}\n")

    def write(self):
        for parser in self.parsers:
            parser.write()

