class ProductionCompany(object):
    # Used by a set to allow only one instance per id
    def __init__(self, production_company_id, name):
        self.production_company_id = production_company_id
        self.name = name

    def to_dict(self):
        return {
            "productioncompanyid": self.production_company_id,
            "productioncompanyname": self.name
        }

    def __eq__(self, other):
        return isinstance(other, ProductionCompany) and self.production_company_id == other.production_company_id

    def __hash__(self):
        return hash(self.production_company_id)