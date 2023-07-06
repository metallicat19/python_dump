import csv


def main():
    class Item:
        pay_rate = 0.8
        all = []

        def __init__(self, name: str, price: float, quantity=0):
            assert price >= 0, f"price {price} can't be equal or smaller than '0'"
            assert quantity >= 0, f"quantity {quantity} can't be equal or smaller than '0'"

            self.name = name
            self.price = price
            self.quantity = quantity

            Item.all.append(self)

        def calculate_total_price(self):
            return self.price * self.quantity

        def apply_discount(self):
            self.price *= Item.pay_rate

        @classmethod
        def instantiate_from_csv(cls):
            with open('items.csv', 'r') as f:
                items = list(csv.DictReader(f))

            for item in items:
                Item(name=item.get('name'), price=float(item.get('price')), quantity=int(item.get('quantity')))

        @staticmethod
        def is_integer(num):
            return num.is_integer() if isinstance(num, float) else isinstance(num, int)

        def __repr__(self):
            return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    class Phone(Item):
        def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
            super().__init__(name, price, quantity)
            assert broken_phones >= 0, f"broken phones {broken_phones} can't be equal or smaller than '0'"

            self.broken_phones = broken_phones

    phone1 = Phone("phone10", 500, 5, 1)

    print(Item.all)
    print(Phone.all)


if __name__ == '__main__':
    main()
