import allure
from selene import browser, be, have


class BookPage:
    @allure.step("Open the book page")
    def open(self, book):
        browser.open(f"book/{book.url}")
        return self

    @allure.step("Adding the selected book to the cart")
    def adding_book_to_cart(self):
        browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()
        browser.driver.refresh()
        return self

    @allure.step("Checking that the book has been added to the cart")
    def book_must_be_added_to_cart(self, book):
        with allure.step("Go to basket"):
            browser.element('[data-testid="tab-basket"]').should(be.visible).click()
        browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text(book.name))
        browser.element('[data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(book.author))
        browser.element('[data-testid="cart__bookCardDiscount--wrapper"]').should(have.text(book.price))
        return self

    @allure.step("Checking that the books has been added to the cart")
    def books_must_be_added_to_cart(self, book1, book2):
        with allure.step("Go to basket"):
            browser.element('[data-testid="tab-basket"]').should(be.visible).click()
        with allure.step("Checking book2"):
            browser.element(f'h3 > a[href="/book/{book2.url}"]').should(have.text(book2.name))
            browser.element('div:nth-child(1) > [data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(book2.author))
            browser.element('div:nth-child(1) > [data-testid="cart__bookCardDiscount--wrapper"]').should(have.text(book2.price))
        with allure.step("Checking book1"):
            browser.element(f'h3 > a[href="/book/{book1.url}"]').should(have.text(book1.name))
            browser.element('div:nth-child(2) > [data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(book1.author))
            browser.element('div:nth-child(2) > [data-testid="cart__bookCardDiscount--wrapper"]').should(have.text(book1.price))
        return self

    @allure.step("Adding a book to favorites")
    def adding_book_to_favorites(self):
        browser.element('ul > li:nth-child(2) > button > div').should(be.visible).click()
        return self

    @allure.step("Checking that the book has been added to favorites")
    def book_must_be_added_to_favorites(self, book):
        with allure.step("Open the favorites"):
            browser.open("my-books/liked/")
        with allure.step("Checking the name, author of the book"):
            browser.element('[data-testid="art__title"]').should(have.text(book.name))
            browser.element('[data-testid="art__authorName"]').should(have.text(book.author))
        return self

    @allure.step("Removing a book to favorites")
    def removing_book_from_favorites(self):
        with allure.step("Open the favorites"):
            browser.open("my-books/liked/")
        with allure.step("Context menu"):
            browser.element('[data-testid="art__wrapper"] [data-testid="popover__baseElement"]').should(be.visible).click()
        with allure.step("Remove from favorites"):
            browser.element('[data-testid="popover__content"] div:nth-child(3)').should(be.visible).click()
        return self

    @allure.step("Checking that the book has been removed from favorites")
    def book_must_be_removed_from_favorites(self):
        browser.element('[data-testid="myBooks__emptyState"]').should(have.text('Здесь будет все, что вы отложите на потом'))
        return self


book_page = BookPage()
