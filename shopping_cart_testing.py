import unittest 
from shopping_cart import calculate_total

""""
Week 31 assignment
"""

class TestShoppingCart(unittest.TestCase):
    def test_calculate_total(self):
        cart = [{'name': 'Item A', 'price': 10.99}]
        result = calculate_total(cart)
        self.assertEqual(result, 10.99)

    def test_calculate_multiple_totals(self):
        cart = [       
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ] 
        result = calculate_total(cart)
        check_total = 10.99 + 5.99 + 8.49
        self.assertEqual(result, check_total)

if __name__ == '__main__':
   unittest.main()
