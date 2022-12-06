#!/usr/bin/env python3

import sys
from collections import Counter

price_map = {'soup'   : 65,
             'bread'  : 80,
             'milk'   : 130,
             'apples' : 100}

def check_input(args: list) -> list:
    
    """
    Function checks that the input groceries are in the list of
    groceries available in the shop (price_map) and returns a
    list of inputs witheach input formatted to lower case
    
    Args:
        args: list - list of groceries input
    
    Raises:
        ValueError - if any groceries detected are not in the price_map
        
    Returns:
        l_lower: list - list of original inputs lowercase
    """
    
    l_lower = list(map(str.lower, args))
    
    invalid_input = [x for x in args if x.lower() not in price_map]
    
    if invalid_input:
        raise ValueError(f"Products ({', '.join(invalid_input)}) are not available in the store")
    
    return l_lower

def get_basket_count(args: list) -> Counter:
    
    """
    Function returns a Counter object constructed
    from input args list
    
    Args:
        args: list - list of groceries input
        
    Returns:
        Counter(args): Counter
    """
    
    return Counter(args)

def sub_total(c: Counter) -> int:
    
    """
    Function calculates subtotal of a basket of groceries without discounts
    
    Args:
        c: Counter - Counter of groceries
    
    Returns:
        sub_total: int - a subtotal value
    """
    
    sub_total = sum(y*price_map.get(x, 0) for x,y in c.items())
    print(f"Subtotal: £{sub_total/100:.2f}")
    
    return sub_total

def discounts(c: Counter) -> int:
    
    """
    Function calculates discount value of the groceries basket
    Current offers are:
    10% discount for apples
    50% discount on bread for every 2 cans of soup
    
    Args:
        c: Counter - Counter of groceries
    
    Returns:
        discount value: int
    """
    
    discount_value = 0
    
    #discount calculation:
    #10*c.get('apples', 0) + 40*min(c.get('soup', 0)//2, c.get('bread',0))
    
    if 'apples' in c:
        apples_discount = 10*c.get('apples', 0)
        print(f"Apples 10% off: {apples_discount}p")
        discount_value += apples_discount
    
    if c.get('soup', 0) >= 2:
        bread_discount = 40*min(c.get('soup', 0)//2, c.get('bread',0))
        print(f"Bread 50% off for every 2 cans of soup: {bread_discount}p")
        discount_value += bread_discount
        
    return discount_value

def total(c: Counter) -> int:
    
    """
    Function calculate total value of a basket of groceries
    by subtracting discounts from subtotal
    
    Args:
        c: Counter - Counter of groceries
        
    Returns:
        None
    """
    
    total = sub_total(c) - discounts(c) 
    print(f"Total: £{total/100:.2f}")
    

if __name__ == '__main__':
    
    args = check_input(sys.argv[1:])
    c = Counter(args)
    total(c)