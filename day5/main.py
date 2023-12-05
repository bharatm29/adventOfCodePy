import re
import aocd
from aocd.get import os

def get_data():
    # return aocd.get_data(os.getenv("AOC"), 5, 2023).split("\n")
    with open("./input.txt", "r") as f:
        return f.read().split("\n")


def part1(data):
    seed_numbers = [int(i) for i in re.findall(r"\d+", data[0])]
    buff = seed_numbers.copy()

    i = 2
    n = len(data)

    while i < n:
        mapping_to = data[i][:-5].split("-to-")
        i += 1

        while i < n and data[i] != "":
            (destination_range, source_range, range_len) = tuple(
                [int(i) for i in re.findall(r"\d+", data[i])]
            )

            for index, prev_val in enumerate(seed_numbers):
                if source_range <= prev_val < source_range + range_len:
                    buff[index] = destination_range + (prev_val - source_range)

            i += 1

        i += 1

        seed_numbers = buff.copy()

    return min(buff)

def part2(data):
    ranges = re.findall(r"\d+\s\d+", file_data[0])
    seed_numbers = []

    for nums in ranges:
        seeds = nums.split()
        start = int(seeds[0])
        length = int(seeds[1])

        for i in range(start, start + length):
            seed_numbers.append(i)

    buff = seed_numbers.copy()

    i = 2
    n = len(data)

    while i < n:
        mapping_to = data[i][:-5].split("-to-")
        i += 1

        while i < n and data[i] != "":
            (destination_range, source_range, range_len) = tuple(
                [int(i) for i in re.findall(r"\d+", data[i])]
            )

            for index, prev_val in enumerate(seed_numbers):
                if source_range <= prev_val < source_range + range_len:
                    buff[index] = destination_range + (prev_val - source_range)

            i += 1

        i += 1

        seed_numbers = buff.copy()

    return min(buff)


if __name__ == "__main__":
    file_data = get_data()

    # p1 = part1(file_data)
    # print(f"Part1: {p1}")

    p2 = part2(file_data)
    print(f"Part2: {p2}")
