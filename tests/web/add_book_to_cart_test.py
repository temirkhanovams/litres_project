import allure
from litres_project.data.books import Book
from litres_project.pages.web.book_page import book_page


@allure.epic('Add book to cart')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking whether a book has been added to cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_adding_book_to_cart():

    book = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-poteryannaya-sestra-69175546/',
        price='339 ₽'
    )

    book_page.open(book)
    book_page.adding_book_to_cart()
    book_page.book_must_be_added_to_cart(book)


@allure.epic('Add book to cart')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking whether a books has been added to cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_adding_books_to_cart():

    book1 = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-poteryannaya-sestra-69175546/',
        price='339 ₽'
    )

    book2 = Book(
        name='Семь сестер. Сестра тени',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-sestra-teni-57182608/',
        price='499 ₽'
    )

    book_page.open(book1)
    book_page.adding_book_to_cart()
    book_page.open(book2)
    book_page.adding_book_to_cart()
    book_page.books_must_be_added_to_cart(book1, book2)
