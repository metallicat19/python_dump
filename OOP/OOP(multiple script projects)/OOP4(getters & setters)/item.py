import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"price {price} can't be equal or smaller than '0'"
        assert quantity >= 0, f"quantity {quantity} can't be equal or smaller than '0'"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long')
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_increment(self, increment_value):
        self.__price += self.price * increment_value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price *= Item.pay_rate

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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times
        Regards, aziz
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect(123456)
        self.__prepare_body()
        self.__send()
