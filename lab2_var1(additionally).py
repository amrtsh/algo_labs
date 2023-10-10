def feed_hamsters(S, hamsters):
    hamsters.sort(key=lambda x: (x[1], -x[0]))
    total_food_needed = 0
    max_hamsters = 0

    for daily_norm, greed in hamsters:
        food_needed = daily_norm + greed * max_hamsters
        if total_food_needed + food_needed <= S:
            total_food_needed += food_needed
            max_hamsters += 1
        else:
            break

    return max_hamsters


def new_func():
    S = int(input("Enter the daily food supply: "))
    C = int(input("Enter the total number of hamsters: "))
    hamsters = []

    for i in range(C):
        daily_norm, greed = map(int, input(f"Enter daily norm and greed for hamster: ").split())
        hamsters.append((daily_norm, greed))

    result = feed_hamsters(S, hamsters)
    print(f"Maximum number of hamsters you can feed: {result}")


if __name__ == '__main__':
    new_func()
