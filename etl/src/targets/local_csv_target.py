class LocalCSVTarget(object):
    def __init__(self, path):
        self.path = path

    #takes a list of dicts
    #extract keys and then write values
    #assumes keys in consistent ordering in dicts as well
    def write(self, items):
        with open(self.path, "w") as target_file:
            headers = []
            print_headers = True

            for item in items:
                line = []
                for key, val in item.items():
                    if print_headers:
                        headers.append(key)
                    line.append(val)

                if print_headers:
                    target_file.write(self.list_to_csv_string(headers))
                    print_headers = False
                    
                target_file.write(self.list_to_csv_string(line))

    def list_to_csv_string(self, collection):
        return ",".join(map(str, collection)) + "\n"