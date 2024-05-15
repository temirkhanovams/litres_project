import allure

from litres_project.data.books import Book
from litres_project.pages.web.book_page import book_page
from litres_project.pages.web.cart_page import cart_page


@allure.epic('Remove book from cart')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking whether a book has been removed from cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_removing_book_from_cart():

    book = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-poteryannaya-sestra-69175546/',
        price='339 ₽'
    )

    book_page.open(book)
    book_page.adding_book_to_cart()
    cart_page.open()
    cart_page.removing_book_to_cart()
    cart_page.book_must_be_removed_from_cart()


@allure.epic('Remove book from cart')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking whether a book has been removed from cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_removing_book_from_cart_and_adding_to_favorites():

    book = Book(
        name='Семь сестер. Потерянная сестра',
        author='Люсинда Райли',
        url='lusinda-rayli/sem-sester-poteryannaya-sestra-69175546/',
        price='339 ₽'
    )

    book_page.open(book)
    book_page.adding_book_to_cart()
    cart_page.open()
    cart_page.removing_book_to_cart_and_adding_to_favorites()
    cart_page.book_must_be_removed_from_cart()
    book_page.book_must_be_added_to_favorites(book)
