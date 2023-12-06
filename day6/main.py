import re


def get_data():
    with open("input.txt", "r") as f:
        return f.read().split("\n")


def find_ways(time: int, dist: int):
    ways = 0

    for i in range(1, time + 1):
        new_dist = i * (time - i)
        if new_dist > dist:
            ways += 1

    return ways


def part1(data):
    times = [int(i) for i in re.findall(r"\d+", data[0])]
    distances = [int(i) for i in re.findall(r"\d+", data[1])]

    ans = 1

    for time, dist in zip(times, distances):
        ans *= find_ways(time, dist)

    return ans

def part2(data):
    time = int("".join(re.findall(r"\d+", data[0])))
    distance = int("".join(re.findall(r"\d+", data[1])))

    return find_ways(time, distance)


if __name__ == '__main__':
    file_data = get_data()
    p1 = part1(file_data)
    p2 = part2(file_data)
    print(f"Part1: {p1}, Part2: {p2}")
