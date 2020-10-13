import json

class LocalJSONTarget(object):
    def __init__(self, path):
        self.path = path

    def write(self, items):
        with open(self.path, "w") as target_file:
            json.dump(items, target_file)