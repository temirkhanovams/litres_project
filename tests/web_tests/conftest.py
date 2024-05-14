from litres_project.helper import attach_web
import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver


@allure.step('Load env')
@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser.config.base_url = 'https://www.litres.ru/'
    browser.config.timeout = 5.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    driver_options = webdriver.ChromeOptions()

    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield browser
    with allure.step('Add screenshot'):
        attach_web.add_screenshot(browser)
    with allure.step('Add slog'):
        attach_web.add_logs(browser)
    with allure.step('Add HTML'):
        attach_web.add_html(browser)
    with allure.step('Add VIDEO'):
        attach_web.add_video(browser)

    browser.quit()