delivery_partner = "Swiggy"

def hotel():
    item = "Pizza"
    def order():
        quantity = 2
        print(f"ordering {quantity} {item} using {delivery_partner}")
    order()
hotel()

print(__file__.upper())