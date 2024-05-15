import allure

import requests

from litres_project.helper.logging_api import logging_api
from tests.api.conftest import base_url


def api_get(url, **kwargs):
    with allure.step("API Request"):
        result = requests.get(base_url + url, **kwargs)
        logging_api(result)
        return result


def api_post(url, **kwargs):
    with allure.step("API Request"):
        result = requests.post(base_url + url, **kwargs)
        logging_api(result)
        return result


def api_put(url, **kwargs):
    with allure.step("API Request"):
        result = requests.put(base_url + url, **kwargs)
        logging_api(result)
        return result
