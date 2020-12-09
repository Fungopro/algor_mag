# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from parso.parser import Stack


def func(list):
    # Use a breakpoint in the code line below to debug your script.
    st = Stack()
    opened = 0
    for item in list:
        # print(item)
        if item == '(':
            st.append(1)
            # print('open')
        elif item == ')' and len(st) != 0:
            # try:
            st.pop()
            print('close')
        else:
            print(opened)
            # print('nothing')
    if len(st):
        print('error')
    print(st)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    func('())(, ((())))')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
