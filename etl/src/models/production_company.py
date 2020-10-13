class ProductionCompany(object):
    # Used by a set to allow only one instance per id
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "productioncompanyid": self.id,
            "productioncompanyname": self.name
        }

    def __eq__(self, other):
        return isinstance(other, ProductionCompany) and self.id == other.id

    def __hash__(self):
        return hash(self.id)