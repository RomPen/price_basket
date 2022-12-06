import pytest

from collections import Counter
from price_basket import check_input, sub_total, discounts


@pytest.mark.parametrize("args, expected", [
    (['soup', 'BREAD'], ['soup', 'bread']),
    (['APPLES', 'Apples', 'ApPlEs'], ['apples', 'apples', 'apples'])
])
def test_check_input(args, expected):
    
    assert check_input(args) == expected
    
@pytest.mark.parametrize("args", [
    ['a', 'b'],
    ['Apples', 'Bananas', 'Coconut']
])
def test_check_input_error(args):
    
    with pytest.raises(ValueError):
        check_input(args)

@pytest.mark.parametrize("c, expected", [
    (Counter(['soup', 'bread']), 145),
    (Counter(['soup', 'soup', 'bread']), 210),
    (Counter(['apples', 'milk', 'soup']), 295),
    (Counter(['soup', 'soup', 'soup', 'soup', 'bread', 'bread', 'bread']), 500)
])
def test_sub_total(c, expected):
    
    assert sub_total(c) == expected

@pytest.mark.parametrize("c, expected", [
    (Counter(['soup', 'bread']), 0),
    (Counter(['soup', 'soup', 'bread']), 40),
    (Counter(['apples', 'milk', 'soup']), 10),
    (Counter(['soup', 'soup', 'soup', 'soup', 'bread', 'bread', 'bread']), 80)
])
def test_discounts(c, expected):
    
    assert discounts(c) == expected
