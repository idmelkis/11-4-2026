# Fails pieejams: https://s.ayy.lv/ff
products = ["apple", "bread", "milk", "cheese"]
prices = [0.80, 1.50, 1.20, 3.50]

def produktu_izvadīšana(products):
    print("\nAvailable products:")
    for i in range(len(products)):
        print(f"{products[i]} - €{prices}")

# Sadalat doto kodu funkcijās:
def produktu_ievade(products, prices):
    cart_products = []
    cart_prices = []
    while True:
        product = input("\nEnter product (or 'done' to finish): ").lower()

        if product == "done":
            break

        if product not in products:
            print("Product not found!")
            continue

        index = products.index(product)
        price = prices[index]

        cart_products.append(product)
        cart_prices.append(price)

        print(f"Added {product} - €{price:.2f}")
    return cart_prices, cart_products

def izvadīt_grozu(cart_products, cart_prices):
    print("\n=== YOUR CART ===")
    for i in range(len(cart_products)):
        print(f"{i + 1}. {cart_products[i]} - €{cart_prices}")

def aprēķināt_groza_kopsummu(cart_prices):
    total = 0
    for price in cart_prices:
        total = total + price
    print(f"\nTotal: €{total}")
    return total
def aprēķināt_atlaidi(total):
    if total >= 20:
        discount = total * 0.10
        print("You receive a 10% discount!")
    elif total >= 10:
        discount = total * 0.05
        print("You receive a 5% discount!")
    else:
        discount = 0
        print("No discount.")
    return discount
def maksājums(final_price):
    payment = float(input("\nEnter payment amount: €"))

    while payment < final_price:
        print("Not enough money!")

        missing = final_price - payment
        print(f"You are missing €{missing:.2f}")

        payment = float(input("Enter payment amount: €"))
    return payment

produktu_izvadīšana(products)
cart_prices, cart_products = produktu_ievade(products, prices)
izvadīt_grozu(cart_products, cart_prices)
total = aprēķināt_groza_kopsummu(cart_prices)
discount = aprēķināt_atlaidi(total)
final_price = total - discount
print(f"Discount: €{discount:.2f}")
print(f"Final price: €{final_price:.2f}")
payment = maksājums(final_price)
change = payment - final_price
izvadīt_grozu(cart_products, cart_prices)

print(f"\nTotal: €{total:.2f}")
print(f"Discount: €{discount:.2f}")
print(f"Paid: €{payment:.2f}")
print(f"Change: €{change:.2f}")

print("\nThank you for shopping!")