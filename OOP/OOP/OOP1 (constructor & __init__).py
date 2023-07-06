def main():
    class Item:
        payrate = 0.8
        all = []

        def __init__(self, name: str, price: float, quantity=0):
            # run validations to received arguments
            assert price >= 0, f'Price {price} can\'t be less than 0!'
            assert quantity >= 0, f'Quantity {quantity} can\'t be less than 0!'

            # initialize class attributes
            self.name = name
            self.price = price
            self.quantity = 0

            # actions to execute
            Item.all.append(self)

        def calculate_total_price(self):
            return self.price * self.quantity

        def apply_discount(self):
            self.price *= self.payrate

        def __repr__(self):
            return f'Item("{self.name}", {self.price}, {self.quantity})'

    item1 = Item("Phone", 100, 1)
    item2 = Item("Laptop", 1000, 3)
    item3 = Item("Cable", 10, 5)
    item4 = Item("Mouse", 50, 5)
    item5 = Item("Keyboard", 75, 5)

    print(Item.all)


if __name__ == '__main__':
    main()
