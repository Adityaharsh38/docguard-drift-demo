def calculate_discount(price, discount):
    """
    Calculate final price with a maximum discount of 20%.
    """
    discount = min(discount, 20)
    return price - (price * discount / 100)
