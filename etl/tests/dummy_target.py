class DummyTarget(object):
    def __init__(self):
        self.items = []

    def write(self, items):
        self.items = items