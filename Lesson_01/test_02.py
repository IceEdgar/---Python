import pytest
from soap_1 import check_text


def test_1(good_word, bad_word):
    assert good_word in check_text(bad_word)

if __name__ == '__name__':
    pytest.main(['-vv'])
