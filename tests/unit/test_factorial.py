import pytest
from src.factorial import fact,div,stest_sum

def test_fact():
    res = fact(5)
    assert res == 120
    res1 = fact(7)
    assert res1 == 5040
    assert fact(0) == 1
    
def test_div():
    result = div(11)
    assert result == 3
    assert div(2) == 16.5
    assert div(10) == 3.3
    
def test_sum():
    result = stest_sum((5,6,-9))
    assert result == 2
    assert stest_sum((-5,20,-9)) == 6
