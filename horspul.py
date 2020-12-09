string =    'asdgdlfkgjsldkjgl;ksdajfg;skdjfg;lksdjfg;ksdjf;gkjsdf;lkgjsd;lkgjsd;lkfjg;lskdjg;lksdfjg;lksdjf;g'
substring = 'ksdajfg;skdjfg;lksdjfg'


def horspul(s, ss):
    len_ss = len(ss)-1
    len_s = len(s)-1
    if len(s) < len(ss):
        return 0
    i = 0
    while i + len_ss < len_s:
        res = False
        for ii in range(0, len_ss):
            if s[i+ii] != ss[ii]:
                res = True

        if res:
            j = 0
            for ri in reversed(range(0, len_ss)):
                if s[i+len_ss] == ss[ri]:
                    i += len_ss - ri
                    break
        else:
            return i+1
        # else:


if __name__ == '__main__':
    print(horspul(string, substring))

