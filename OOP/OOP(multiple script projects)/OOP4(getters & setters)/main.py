from phone import Phone


def main():
    item1 = Phone('phone', 1000, 3)

    item1.apply_increment(0.2)

    print(item1.price)


if __name__ == '__main__':
    main()
