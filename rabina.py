string = 'abbabababaaababaabababbaaabbbbaabbbaabbbabbbaabbaabbababbababaaaba'


def func_rabin_karp(source, substring):
    hash_str = hash(source[:len(substring)])
    hash_substr = hash(substring)
    res = []
    for i in range(0, len(source)):
        if hash_str == hash_substr:
            res.append(i)
        hash_str = hash(source[i:i+len(substring)])
    return  res


if __name__ == '__main__':
    subsrt = 'aabbb'
    print('res',func_rabin_karp(string, subsrt))
