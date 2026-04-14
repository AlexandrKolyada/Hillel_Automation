import requests
import pytest
from requests.auth import HTTPBasicAuth
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('test_search.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    url = 'http://127.0.0.1:8080/auth'
    response = session.post(url, auth=HTTPBasicAuth('test_user', 'test_pass'))
    token = response.json().get('access_token')
    session.headers.update({'Authorization': f'Bearer {token}'})
    logger.info("Authorization successful, token added to session")
    return session

@pytest.mark.parametrize("sort_by, limit", [('year', 2), ('engine_volume', 3), ('price', 4)])
def test_car_search( auth_session, sort_by, limit):
    url = 'http://127.0.0.1:8080/cars'
    response = auth_session.get(url, params={'sort_by': sort_by, 'limit': limit})
    logger.info(f"sort_by = {sort_by}, limit = {limit}")
    assert response.status_code == 200
    data = response.json()
    logger.info(f"Received {len(data)} cars from server")
    assert len(data) == limit, f"Expected{limit}, but got {len(data)}"