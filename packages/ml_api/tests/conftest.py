import pytest


from packages.ml_api.api.app import create_app
from packages.ml_api.api.config import TestingConfig


@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client
