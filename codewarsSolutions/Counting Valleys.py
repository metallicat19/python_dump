# 7kyu
def main():
    def counting_valleys(s):
        level = total_enter = total_exit = 0
        in_valley = False

        for c in s:
            level += 1 if c == 'U' else -1 if c == 'D' else 0
            if level < 0 and not in_valley:
                total_enter += 1
                in_valley = True

            elif level >= 0 and in_valley:
                total_exit += 1
                in_valley = False

        return (total_enter + total_exit) // 2

    print(counting_valleys('DFFFU'))


if __name__ == '__main__':
    main()
