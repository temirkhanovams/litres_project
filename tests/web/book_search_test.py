import allure

from litres_project.data.books import Book
from litres_project.pages.web.main_page import main_page


@allure.epic('Search')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking the book search on the main page")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_searching_of_book_by_title():
    book = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='',
        price=''
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Enter the name of the book in the search and click the Find button"):
        main_page.search_book_by_title(book)

    with allure.step("Checking that books with the specified title are found in the search"):
        main_page.book_with_specified_title_must_be_found()


@allure.epic('Search')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking the book search on the main page")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_searching_of_book_by_author():
    book = Book(
        name='',
        author='Люсинда Райли',
        url='',
        price=''
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Enter the author of the book in the search and click the Find button"):
        main_page.search_book_by_author(book)

    with allure.step("Checking that books with the specified author are found in the search"):
        main_page.book_with_specified_author_must_be_found(book)
