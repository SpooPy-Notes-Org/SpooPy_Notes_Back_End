from app.spoopy import *

import pytest


# ========
# FIXTURES
# ========

@pytest.fixture
def paths():
    return generate_paths('hi there')


@pytest.fixture
def words():
    input_paths = ['app/assets/a_1.png', ' ', 'app/assets/b_2.png', 'app/assets/c_1.png', 'app/assets/punctuation_1/exclaimation_1.png']
    return create_word_dictionaries(input_paths)


@pytest.fixture
def lines(words):
    return create_lines(words)


@pytest.fixture
def coords(lines):
    return determine_background(lines)


# =====
# TESTS
# =====

def test_generate_paths_exists():
    assert generate_paths


def test_generate_paths():
    # Not asserting randomness of the return value
    actual = generate_paths('abc')
    assert len(actual) == 3

    actual = generate_paths('ABC')
    assert len(actual) == 3

    actual = generate_paths('1234')
    assert len(actual) == 4


def test_generate_paths_special_chars():
    actual = generate_paths('!.')
    assert len(actual) == 2


def test_create_word_dictionaries(paths):
    actual = create_word_dictionaries(paths)
    assert len(actual) == 2
    assert actual[0]['height']
    assert actual[0]['width']


def test_create_lines(words):
    actual = create_lines(words)
    assert len(actual) == 1


def test_determine_background(lines):
    actual = determine_background(lines)
    assert actual == (521, 167)


def test_compose_image(lines, coords):
    width, height = coords
    actual = compose_image(width, height, lines, 900)
    assert actual != ''