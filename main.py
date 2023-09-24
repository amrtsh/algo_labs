def second_level(input_arr):
    asc = desc = True
    for index in range(len(input_arr) - 1):
        if input_arr[index] <= input_arr[index + 1]:
            desc = False
        elif input_arr[index] >= input_arr[index + 1]:
            asc = False
    return asc or desc


if __name__ == '__main__':
    input_arr = [5, 4, 3, 2, 1]
    print(second_level(input_arr))
