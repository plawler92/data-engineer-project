class MovieTransformer(object):
    def __init__(self, source, parsers):
        self.source = source
        self.parsers = parsers

    # Reads from source and send the row through each parsers
    # applied to this transformer
    def transform(self):
        for row in self.source.read():
            for parser in self.parsers:
                parser.parse(row)

    def write(self):
        for parser in self.parsers:
            parser.write()

