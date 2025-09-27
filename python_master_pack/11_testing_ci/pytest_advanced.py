"""Advanced pytest patterns: fixtures and parametrize"""
import pytest

@pytest.fixture
def sample_list():
    return [1,2,3]

@pytest.mark.parametrize('a,b,exp', [(1,2,3),(2,3,5)])
def test_add(a,b,exp):
    assert a+b == exp
