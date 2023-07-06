# 5kyu
def main():
    def valid_ISBN10(isbn):
        if len(isbn) == 10 and not isbn.isalpha():
            sum_of_isbn = sum([int(a) * idx for idx, a in enumerate(isbn, start=1) if a.isdigit()])
            if isbn[-1] == 'X':
                sum_of_isbn += 100

            return sum_of_isbn % 11 == 0
        return False

    print(valid_ISBN10('123456789T'))

    """
    a = [i for i in range(10)]
    for idx, a in enumerate(a):
        print(a, idx)
    """


if __name__ == '__main__':
    main()
