import aocd
import os


def get_data():
    """For small input"""
    # with open("./input.txt", "r") as f:
    #     return f.read().split("\n")[:-1]
 
    return aocd.get_data(os.getenv("AOC"), 4, 2023).split("\n")

file_data = get_data()


def determine_points(winning_nums: list[int], drawn_nums: list[int]) -> int:
    points = 0

    for i in drawn_nums:
        if i in winning_nums:
            if points == 0:
                points = 1
            else:
                points *= 2

    return points


def part1(data: list[str]):
    ans = 0

    for line in data:
        colon_partition = line.partition(":")

        num_list = colon_partition[2].partition("|")

        winning_nums = [int(i) for i in num_list[0].split()]
        drawn_nums = [int(i) for i in num_list[2].split()]

        ans += determine_points(winning_nums, drawn_nums)

    return ans


def part2(data: list[str]):
    length = len(data)
    print(length)

    card_instances = [1 for _ in range(length + 1)]
    card_instances[0] = 0

    for line in data:
        colon_partition = line.partition(":")

        cards = colon_partition[0]
        card_number = int(cards.split()[1])

        num_list = colon_partition[2].partition("|")
        winning_nums = [int(_) for _ in num_list[0].split()]
        drawn_nums = [int(_) for _ in num_list[2].split()]

        card_point = len([_ for _ in drawn_nums if _ in winning_nums])


        for i in range(card_number + 1, card_number + card_point + 1):
            if i <= length:
                card_instances[i] += card_instances[card_number]

        print(card_point, card_number, card_instances)


    return sum(card_instances)


if __name__ == "__main__":
    p1 = part1(file_data)
    p2 = part2(file_data)
    print(f"Part1: {p1}, Part2: {p2}")
