import pytest
from app import create_app
from config import Config


class TestConfig(Config):
    pass

@pytest.fixture
def client():
    app = create_app(TestConfig)
    app_context = app.app_context

# @pytest.fixture
# def test_status_200():
#     pass

# @pytest.fixture
# def test_image_type_png():
#     pass

# @pytest.fixture
# def test_query_intake():
#     pass

# @pytest.fixture
# def test_single_letter_to_png():
#     pass

# @pytest.fixture
# def test_image_composer_abc_as_one_png():
#     pass

# @pytest.fixture
# def test_image_composer_spoopy():
#     pass

# @pytest.fixture
# def test_query_to_png():
#     pass

# @pytest.fixture
# def test_image_size_range():
#     pass



#  Stretch - test randomizer?
