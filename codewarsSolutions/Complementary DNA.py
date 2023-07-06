# 7kyu
def main():
    def DNA_strand(dna):  # mine
        dna_copy = ''

        for inst in dna:
            index = 'ATCG'.find(inst)
            dna_copy += 'ATCG'[index + 1] if index % 2 == 0 else 'ATCG'[index - 1]

        return dna_copy

    def DNA_strand1(dna):  # better solution
        return dna.translate(str.maketrans("ATCG", "TAGC"))

    print(DNA_strand1('TGCAT'))


if __name__ == '__main__':
    main()
