from selene import browser, be, have


class CartPage:
    def open(self):
        browser.open('my-books/cart/')
        return self

    def removing_book_to_cart(self):
        browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible).click()
        browser.element('[data-testid="cart__modalDeleteArt"] button:nth-child(1)').should(be.visible).click()
        return self

    def book_must_be_removed_from_cart(self):
        browser.element('[data-testid="cart__emptyState--wrapper"] h2').should(have.text('Корзина пуста'))
        return self

    def removing_book_to_cart_and_adding_to_favorites(self):
        browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible).click()
        browser.element('[data-testid="cart__modalDeleteArt"] button:nth-child(2)').should(be.visible).click()
        return self


cart_page = CartPage()
