arr = [1, 30, 0, 2, 5]


def left_side_smaller(array, n):
    print("_, ", end="")
    # Начать со второго элемента
    for i in range(1, n):
        for j in range(i - 1, -2, -1):
            if array[j] < array[i]:
                print(array[j], ", ", end="")
                break
            if j == -1:
                print("_, ", end="")


if __name__ == '__main__':
    n = len(arr)
    left_side_smaller(arr, n)

