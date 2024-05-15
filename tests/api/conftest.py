import pytest
from dotenv import load_dotenv


base_url = "https://api.litres.ru/foundation/api"


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

