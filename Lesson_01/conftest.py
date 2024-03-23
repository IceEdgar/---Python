import pytest

@pytest.fixture()
def coord():
    return "37.7891838", "-122.4033522"


@pytest.fixture()
def text():
    return "One Montgomery Tower"


@pytest.fixture()
def bad_word():
    return "Короллество"

@pytest.fixture()
def good_word():
    return "Королевство"

@pytest.fixture()
def url():
    return "https://speller.yandex.net/services/spellservice?WSDL"
