op = {'+': lambda x, y: int(x) + int(y),
      '*': lambda x, y: int(x) * int(y),
      '/': lambda x, y: int(x) / int(y),
      '-': lambda x, y: int(x) - int(y),
      '^': lambda x, y: int(x) ^ int(y)}


def func(arr):
    stack = []
    for item in arr:
        if item in op:
            stack.append(op.get(item)(stack.pop(), stack.pop()))
        else:
            stack.append(item)
    return stack[0]


if __name__ == '__main__':
    print(func('3 4 2 * 1 5 - 2 ^ / +'.split(' ')))

