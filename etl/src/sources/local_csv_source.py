import csv

class LocalCSVSource(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, "r") as source_file:
            csv_reader = csv.DictReader(source_file)
            for line in csv_reader:
                yield line