import os
import allure
from litres_project.data.users import User
from litres_project.pages.web.main_page import main_page


@allure.epic('Authorized')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorization_registered_user():

    user = User(
        name='Marina T',
        email=os.getenv('USER_EMAIL'),
        password=os.getenv('USER_PASSWORD')
    )

    main_page.open()
    main_page.filling_authorization_form(user)
    main_page.user_must_be_authorized(user)


@allure.epic('Authorized')
@allure.label("owner", "TemirkhanovaMS")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorization_unregistered_user():

    user = User(
        name='test',
        email=os.getenv('UNREGISTERED_USER_EMAIL'),
        password=os.getenv('UNREGISTERED_USER_PASSWORD')
    )

    main_page.open()
    main_page.filling_authorization_form(user)
    main_page.user_must_not_be_authorized()
