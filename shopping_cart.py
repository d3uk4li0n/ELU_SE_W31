
"""Week 30 assignment"""

def calculate_total(cart):
    """returns amount of items in the cart"""
    total = 0
    #total_items = len(cart)
    for item in cart:
        total += item['price']
    return total

def display_total(total):
    """prints total price"""
    print("Total price: " + total)

CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': '8.49'}
]

"""prints items in cart"""
for thing in CART:
    print(f"Item: {thing['name']} - Price: ${thing['price']}")

shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)
