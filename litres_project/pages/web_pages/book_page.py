from selene import browser, be, have


class BookPage:
    def open(self, book):
        browser.open(f"book/{book.url}")
        return self

    def adding_book_to_cart(self):
        browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()
        # browser.driver.refresh()
        return self

    def book_must_be_added_to_cart(self, book):
        browser.open("my-books/cart/")
        browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text(book.name))
        browser.element('[data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(book.author))
        browser.element('[data-testid="cart__bookCardDiscount--wrapper"]').should(have.text(book.price))
        return self

    def adding_books_to_cart(self):
        browser.element('[data-test-id="book__addToCartButton--desktop"]').should(be.visible).click()
        browser.driver.refresh()
        return self

    def books_must_be_added_to_cart(self, book1, book2):
        browser.open("my-books/cart/")
        browser.element(f'h3 > a[href="/book/{book2.url}"]').should(have.text(book2.name))
        browser.element('div:nth-child(1) > [data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(book2.author))
        browser.element('div:nth-child(1) > [data-testid="cart__bookCardDiscount--wrapper"]').should(have.text(book2.price))
        browser.element(f'h3 > a[href="/book/{book1.url}"]').should(have.text(book1.name))
        browser.element('div:nth-child(2) > [data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(book1.author))
        browser.element('div:nth-child(2) > [data-testid="cart__bookCardDiscount--wrapper"]').should(have.text(book1.price))
        return self

    def adding_book_to_favorites(self):
        browser.element('ul > li:nth-child(2) > button > div').should(be.visible).click()
        return self

    def book_must_be_added_to_favorites(self, book):
        browser.open("my-books/liked/")
        browser.element('[data-testid="art__title"]').should(have.text(book.name))
        browser.element('[data-testid="art__authorName"]').should(have.text(book.author))
        return self

    def removing_book_from_favorites(self):
        browser.open("my-books/liked/")
        browser.element('[data-testid="art__wrapper"] [data-testid="popover__baseElement"]').should(be.visible).click()
        browser.element('[data-testid="popover__content"] div:nth-child(3)').should(be.visible).click()
        return self

    def book_must_be_removed_from_favorites(self):
        browser.element('[data-testid="myBooks__emptyState"]').should(have.text('Здесь будет все, что вы '
                                                                                     'отложите на потом'))
        return self


book_page = BookPage()
