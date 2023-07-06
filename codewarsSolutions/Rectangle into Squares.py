# 6kyu

def main():
    def sq_in_rect(lng, wdth):

        a = [lng if lng < wdth else wdth]

        if lng != wdth:
            large = lng if lng > wdth else wdth
            small = lng if lng < wdth else wdth
            a.extend(sq_in_rect(large - small, small))
            return a

        else:
            a = [lng] if len(a) > 1 else None
            return a

    print(sq_in_rect(5, 7))


if __name__ == '__main__':
    main()
