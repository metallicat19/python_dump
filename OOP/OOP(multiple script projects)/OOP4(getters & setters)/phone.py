from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"broken phones {broken_phones} can't be equal or smaller than '0'"

        self.broken_phones = broken_phones
