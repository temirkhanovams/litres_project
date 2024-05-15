from selene import browser, be, have
import allure


class CartPage:
    @allure.step("Open the cart page")
    def open(self):
        browser.open('my-books/cart/')
        return self

    @allure.step("Removing the selected book from cart")
    def removing_book_to_cart(self):
        browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible).click()
        browser.element('[data-testid="cart__modalDeleteArt"] button:nth-child(1)').should(be.visible).click()
        return self

    @allure.step("Checking that the book has been removed from cart")
    def book_must_be_removed_from_cart(self):
        browser.element('[data-testid="cart__emptyState--wrapper"] h2').should(have.text('Корзина пуста'))
        return self

    @allure.step("Removing the selected book from cart and adding book to favorites")
    def removing_book_to_cart_and_adding_to_favorites(self):
        browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible).click()
        browser.element('[data-testid="cart__modalDeleteArt"] button:nth-child(2)').should(be.visible).click()
        return self


cart_page = CartPage()
