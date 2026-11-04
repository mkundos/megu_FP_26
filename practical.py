# Практична робота за заняттями 1–6. «Каса крамниці»
# Шапран Геннадій  Група: ПІ-24

CARD = 17

cart = [120, 1000, 45, 300]

print(len(cart))  


def item_cost(price, quantity):
    return price * quantity


 
def item_cost_with_packing(price, quantity, packing):
    return item_cost(price, quantity) + packing


def discount_price(price):
    if price >= 1000:
        return price - price * 25 / 100
    else:
        return price


def delivery_cost(total):
    if total >= 800:
        return 0
    else:
        return 35


def add_item(cart, price):
    return cart + [price]



def discounted_all(cart):
    return [discount_price(p) for p in cart]



def cart_total(cart):
    return sum(cart)



def receipt_total(cart):
    total = cart_total(discounted_all(cart))
    return total + delivery_cost(total)




fee = 40


def price_with_fee(price, fee):
    return price + fee


def add_gift(cart):
    return cart + [0]



def savings(cart):
    return cart_total(cart) - cart_total(discounted_all(cart))