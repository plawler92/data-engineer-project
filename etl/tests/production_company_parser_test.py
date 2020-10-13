import pytest

from src.parsers import ProductionCompanyParser
from src.models import ProductionCompany
from tests.dummy_target import DummyTarget

def test_production_company_parse_succeeds():
    movie_id = 1
    production_company_id = 15
    production_company_name = "Test Studios"

    movie = create_production_company_str(movie_id, production_company_id, production_company_name)

    dummy_company_target = DummyTarget()
    dummy_join_target = DummyTarget()
    production_company_parser = ProductionCompanyParser(dummy_company_target, dummy_join_target)

    production_company_parser.parse(movie)
    production_company_parser.write()

    company_result = dummy_company_target.items[0]
    join_result = dummy_join_target.items[0]

    assert company_result["productioncompanyid"] == production_company_id
    assert company_result["productioncompanyname"] == production_company_name
    assert join_result["movieid"] == movie_id
    assert join_result["productioncompanyid"] == production_company_id

def create_production_company_str(movie_id, production_company_id, production_company_name):
    return {
        'id': str(movie_id),
        'production_companies': "[{'id': '" + str(production_company_id) + "', 'name': '" + production_company_name + "'}]"
    }