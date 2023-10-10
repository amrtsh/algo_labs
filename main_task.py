def square_board(number: int, width: int, height: int) -> int:
    left, right = 1, max(width, height) * number
    counter = 0  # додано під час здачі лабораторної для визначення кількості ітерацій

    while left < right:
        mid = left + (right - left) // 2
        columns = mid // width
        rows = mid // height
        sheets = columns * rows

        if sheets >= number:
            right = mid
        else:
            left = mid + 1
        counter += 1
    print(counter)
    return left


def new_func():
    number = int(input("Enter the number of sheets: "))
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    # result = square_board(number, width, height)
    # print(result)
    if 1 <= number <= 1012 and 1 <= width <= 109 and 1 <= height <= 109:
        result = square_board(number, width, height)
        print(result)
    else:
        print("Invalid input values.")


if __name__ == '__main__':
    new_func()
