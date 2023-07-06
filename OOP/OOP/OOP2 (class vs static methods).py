import csv


def main():
    class Item:
        pay_rate = 0.8
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
            self.price *= self.pay_rate

        @classmethod
        def instantiate_from_csv(cls):
            with open('items.csv', 'r') as f:
                reader = csv.DictReader(f)
                items = list(reader)

            for item in items:
                Item(name=item.get('name'), price=float(item.get('price')), quantity=int(item.get('quantity')))

        @staticmethod
        def is_integer(num):
            return num.is_integer() if isinstance(num, float) else isinstance(num, int)

        def __repr__(self):
            return f'Item("{self.name}", {self.price}, {self.quantity})'

    Item.instantiate_from_csv()
    print(Item.all)
    print(Item.is_integer(10.0))


if __name__ == '__main__':
    main()
