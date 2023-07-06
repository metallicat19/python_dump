# 6kyu
def main():
    def solution(s):
        split_list = []
        match len(s) % 2:

            case 0:
                for i in range(0, len(s), 2):
                    split_list.append(s[i:i + 2])
                return split_list

            case 1:
                for i in range(0, len(s) - 1, 2):
                    split_list.append(s[i:i + 2])
                split_list.append(s[len(s) - 1:len(s)] + '_')
                return split_list


if __name__ == '__main__':
    main()
