import allure
import jsonschema
from litres_project.helper.load_schema import load_schema
from litres_project.helper.api_requests import api_get


@allure.epic('API. Search')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking the book search on the main page")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_successful_searching_of_book_by_title():
    schema = load_schema('successful_searching_book.json')

    book_title = 'Семь сестер. Потерянная сестра'
    art_types = 'text_book'
    types = 'text_book'
    url = f"/search?q={book_title}&art_types={art_types}&types={types}"
    headers = {"Content-Type": "application/json"}

    result = api_get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['payload']['data'][0]['type'] == "text_book"
    assert result.json()['payload']['data'][0]['instance']['art_type'] == 0
    assert 'Семь сестер' in result.json()['payload']['data'][0]['instance']['title']


@allure.epic('API. Search')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking the book search on the main page")
@allure.label('microservice', 'API')
@allure.label('microservice', 'Search')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_unsuccessful_searching_of_book_by_title():
    schema = load_schema('unsuccessful_searching_book.json')

    book_title = 'nbmcgfhmghm'
    types = 'text_book'
    url = f"/search?q={book_title}&types={types}"
    headers = {"Content-Type": "application/json"}

    result = api_get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['payload']['data']) == 0
