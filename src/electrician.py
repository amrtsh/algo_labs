import math

# Memoization dictionary to store already computed values
memo_dict = {}


def adjust_pillar_height(height_of_pillar, current):
    if current + 1 >= len(height_of_pillar):
        if height_of_pillar[current] > height_of_pillar[current - 1]:
            height_of_pillar[current - 1] = 1
        elif height_of_pillar[current] < height_of_pillar[current - 1]:
            height_of_pillar[current] = 1
        return True
    if (
            height_of_pillar[current - 1] <= height_of_pillar[current]
            and height_of_pillar[current + 1] <= height_of_pillar[current]
    ):
        height_of_pillar[current - 1] = 1
        height_of_pillar[current + 1] = 1
    elif height_of_pillar[current - 1] > height_of_pillar[current]:
        height_of_pillar[current] = 1
    elif (
            height_of_pillar[current + 1] > height_of_pillar[current]
            and height_of_pillar[current - 1] != 1
    ):
        height_of_pillar[current] = 1
    return False


def calculate_distance(height_of_pillar, distance):
    result = 0
    for current in range(1, len(height_of_pillar)):
        difference = height_of_pillar[current] - height_of_pillar[current - 1]
        memo_key = (current, distance)
        if memo_key in memo_dict:
            calc_value = memo_dict[memo_key]
        else:
            calc_value = math.sqrt(distance ** 2 + difference ** 2)
            memo_dict[memo_key] = calc_value
        result += calc_value
    return result


def set_distance(distance, height_of_pillar):
    for current in range(1, len(height_of_pillar)):
        if adjust_pillar_height(height_of_pillar, current):
            break
    result = calculate_distance(height_of_pillar, distance)
    return result


if __name__ == "__main__":
    with open('input.txt', 'r') as r:
        distance: int = int(r.readline())
        height_of_pillar: list = list(map(int, r.readline().split()))

    result = set_distance(distance, height_of_pillar)
    print(result.__round__(2))
