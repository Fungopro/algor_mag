str = 'abbabababaaababaabababbaaabbbbaabbbaabbbabbbaabbaabbababbababaaaba'


def func_knut_morris(str, substring):
    substring = list(substring)

    suffix_arr = [1] * (len(substring) + 1)
    i = 1
    for pos in range(len(substring)):
        while i <= pos and substring[pos] != substring[pos - i]:
            i += suffix_arr[pos-i]
        suffix_arr[pos+1] = i

    i = 0
    count_symbols = 0
    for c in str:
        while count_symbols == len(substring) or \
              count_symbols >= 0 and substring[count_symbols] != c:
            i += suffix_arr[count_symbols]
            count_symbols -= suffix_arr[count_symbols]
        count_symbols += 1
        if count_symbols == len(substring):
            yield i


if __name__ == '__main__':
    subsrt = 'aabbb'
    print([i for i in func_knut_morris(str, subsrt)])
