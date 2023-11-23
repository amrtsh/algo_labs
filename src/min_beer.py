# import os.path
# import itertools
#
# input_file_path = os.path.abspath('input.txt')
#
# with open(input_file_path, 'r') as f:
#     num_of_employees, amount_of_beer_available = map(int, f.readline().strip().split())
#     y_or_n = f.readline().split()
#
#
# def is_valid(num_of_employees, amount_of_beer_available):
#     return 0 < num_of_employees < 50 and 0 <= amount_of_beer_available < 50
#
#
# matrix = [list(beer) for beer in y_or_n]
# result_matrix = list(map(list, zip(*matrix)))
#
# y_indexes = {i: [index for index, value in enumerate(row) if value == 'Y'] for i, row in enumerate(result_matrix)}
#
# for key, value in y_indexes.items():
#     print(f"Row {key}: {value}")
#
# # Чи дорівнює сума унікальних індексів в одному або декількох рядках кількості працівників
# found_solution = False
# for i in range(1, len(y_indexes) + 1):
#     for combination in itertools.combinations(y_indexes.keys(), i):
#         keys_with_no_common_elements = set()
#         for key in combination:
#             keys_with_no_common_elements.update(y_indexes[key])
#         if len(keys_with_no_common_elements) == num_of_employees:
#             print("Rows:", combination)
#             found_solution = True
#             break
#     if found_solution:
#         break


import os.path


def read_input(file_path):
    with open(file_path, 'r') as f:
        num_of_employees, amount_of_beer_available = map(int, f.readline().strip().split())
        y_or_n = f.readline().split()
    return num_of_employees, amount_of_beer_available, y_or_n


def is_valid(num_of_employees, amount_of_beer_available):
    return 0 < num_of_employees < 50 and 0 <= amount_of_beer_available < 50


def create_matrix(y_or_n):
    return [list(beer) for beer in y_or_n]


def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))


def find_y_indexes(result_matrix):
    return {i: [index for index, value in enumerate(row) if value == 'Y'] for i, row in enumerate(result_matrix)}


def generate_combinations(arr, r):
    # arr - вхідний список
    # r -довжина
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        #     ключове слово для повернення значення з генератора
        else:
            for next_comb in generate_combinations(arr[i + 1:], r - 1):
                yield [arr[i]] + next_comb


def find_beer_solution(y_indexes, num_of_employees):
    found_solution = False

    for i in range(1, len(y_indexes) + 1):
        for combination in generate_combinations(list(y_indexes.keys()), i):
            keys_with_no_common_elements = set()
            for key in combination:
                keys_with_no_common_elements.update(y_indexes[key])
            if len(keys_with_no_common_elements) == num_of_employees:
                with open(output_file_path, 'w') as f:
                    f.write(f"{[list(beer) for beer in y_or_n]}\n")
                    f.write(f"{list(map(list, zip(*matrix)))}\n")
                    f.write(f"Rows: {combination}")
                found_solution = True
                break
        if found_solution:
            break


if __name__ == "__main__":
    input_file_path = os.path.abspath('input.txt')
    output_file_path = os.path.abspath('output.txt')
    num_of_employees, amount_of_beer_available, y_or_n = read_input(input_file_path)

    if is_valid(num_of_employees, amount_of_beer_available):
        matrix = create_matrix(y_or_n)
        result_matrix = transpose_matrix(matrix)
        y_indexes = find_y_indexes(result_matrix)

        for key, value in y_indexes.items():
            print(f"Row {key}: {value}")

        find_beer_solution(y_indexes, num_of_employees)
    else:
        print("Input is not valid.")
