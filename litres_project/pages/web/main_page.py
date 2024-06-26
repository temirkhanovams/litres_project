from selene import browser, be, have
from litres_project.helper.input_search_web import press_sequentially
import allure


class MainPage:

    @allure.step("Open the main page")
    def open(self):
        browser.open("")
        return self

    @allure.step("Filling the authorization form")
    def filling_authorization_form(self, user):
        browser.element('[href="/pages/login/"]').should(be.visible).click()
        browser.element('[name="email"]').should(be.visible).type(user.email)
        browser.element('.AuthContent_form__submit__LzXKD > [type="submit"]').should(be.visible).click()
        browser.element('[name="pwd"]').should(be.visible).type(user.password)
        browser.element('.AuthContent_form__submit__LzXKD > [type="submit"]').should(be.visible).click()
        return self

    @allure.step("Checking that user has been authorized")
    def user_must_be_authorized(self, user):
        browser.element('[data-testid="header__profile-button"]').should(be.visible).click()
        browser.open("pages/personal_cabinet_about_me/")
        browser.element('span[class="user_header__name"]').should(have.text(user.name))
        return self

    @allure.step("Checking that user has not been authorized")
    def user_must_not_be_authorized(self):
        browser.element('.ControlInput_input__error__0DtKl').should(have.text('Неверное сочетание логина и '
                                                                              'пароля'))
        return self

    @allure.step("Enter the name of the book in the search and click the Find button")
    def search_book_by_title(self, book):
        browser.element('[data-testid="search__input"]').click().perform(press_sequentially(f'{book.name}'))
        browser.element('[data-testid="search__button"]').should(be.visible).click()
        return self

    @allure.step("Checking that books with the specified title are found in the search")
    def book_with_specified_title_must_be_found(self):
        browser.element('[data-testid="art__title"]:nth-child(1)').should(have.text('Семь сестер'))
        return self

    @allure.step("Enter the author of the book in the search and click the Find button")
    def search_book_by_author(self, book):
        browser.element('[data-testid="search__input"]').click().perform(press_sequentially(f'{book.author}'))
        browser.element('[data-testid="search__button"]').should(be.visible).click()
        return self

    @allure.step("Checking that books with the specified author are found in the search")
    def book_with_specified_author_must_be_found(self, book):
        browser.element('[data-testid="art__authorName"]:nth-child(1)').should(have.text(book.author))
        return self


main_page = MainPage()
