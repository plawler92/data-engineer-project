import ast
import logging

from src.models import ProductionCompany

class ProductionCompanyParser(object):
    def __init__(self, production_company_target, join_target):
        self.prodcution_company_target = production_company_target
        self.join_target = join_target
        self.production_companies = set()
        self.joins = []

    # Extracts information about production companies and separately combines each movie id with 
    # the associated production company id. In the event a duplicate production company 
    # (based on id) is found only the first instance is stored. If later instances have differing
    # names they are lost in this implementation. This should not occur since the data is based on ids.
    def parse(self, row):
        for production_company in ast.literal_eval(row["production_companies"]):
            production_company_id = int(production_company["id"])
            self.joins.append({
                "movieid": int(row["id"]),
                "productioncompanyid": production_company_id
            })
            self.production_companies.add(ProductionCompany(production_company_id, production_company["name"]))
                
    def write(self):
        self.prodcution_company_target.write([x.to_dict() for x in self.production_companies])
        self.join_target.write(self.joins)
