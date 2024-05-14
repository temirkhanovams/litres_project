import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from litres_project.helper import attach_web
#
# DEFAULT_BROWSER_VERSION = "100.0"
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser_version',
#         default='100.0'
#     )
#
#
# @pytest.fixture(scope="session", autouse=True)
# def load_env():
#     load_dotenv()
#
#
# @pytest.fixture(scope='function', autouse=True)
# def setup_browser(request):
#     browser_version = request.config.getoption('--browser_version')
#     browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
#     options = Options()
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": browser_version,
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#     load_dotenv()
#     login = os.getenv('LOGIN')
#     password = os.getenv('PASSWORD')
#     driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
#                               options=options)
#     browser.config.base_url = "https://www.litres.ru/"
#     browser.config.driver = driver
#     browser.config.driver_options = options
#
#     browser.config.timeout = 4.0
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#
#     yield browser
#
#     attach_web.add_screenshot(browser)
#     attach_web.add_logs(browser)
#     attach_web.add_html(browser)
#     attach_web.add_video(browser)
#
#     browser.quit()


# ########################################3
# #ЛОКАЛЬНО#
#
#
# import allure
# import pytest
# from dotenv import load_dotenv
# from selene import browser
# from selenium import webdriver
#
# # from utils import attach
#
#
# @allure.step('Load env')
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()
#
#
# @pytest.fixture(scope='function', autouse=True)
# def setup_browser(request):
#     browser.config.base_url = 'https://www.litres.ru/'
#     browser.config.timeout = 5.0
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     driver_options = webdriver.ChromeOptions()
#
#     driver_options.page_load_strategy = 'eager'
#     browser.config.driver_options = driver_options
#
#     yield browser
#     with allure.step('Add screenshot'):
#         attach_web.add_screenshot(browser)
#     with allure.step('Add logs'):
#         attach_web.add_logs(browser)
#     with allure.step('Add HTML'):
#         attach_web.add_html(browser)
#     with allure.step('Add VIDEO'):
#         attach_web.add_video(browser)
#
#     browser.quit()


##################
### Jenkins ###
##################

import os

import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver import ChromeOptions

DEFAULT_BROWSER_VERSION = "100.0"


@allure.step('Select browser version')
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser name.")
    parser.addoption('--browser_version', default='100.0',
                     help='Choose browser version. For Chrome: 99.0 or 100.0. For Firefox: 97.0 or 98.0.')


@allure.step('Load env')
@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_name = request.config.getoption('--browser_name')
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    browser_name = 'chrome'
    driver_options = ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://www.litres.ru/'
    browser.config.timeout = 5.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    selenoid_capabilities = {"browserName": browser_name, "browserVersion": browser_version,
                             "selenoid:options": {"enableVNC": True, "enableVideo": True}}

    driver_options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
                              options=driver_options)

    browser.config.driver = driver

    yield browser
    with allure.step('Add screenshot'):
        attach_web.add_screenshot(browser)
    with allure.step('Add logs'):
        attach_web.add_logs(browser)
    with allure.step('Add HTML'):
        attach_web.add_html(browser)
    with allure.step('Add VIDEO'):
        attach_web.add_video(browser)

    browser.quit()
