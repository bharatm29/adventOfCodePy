import os
import aocd


def get_data():
    return aocd.get_data(os.getenv("AOC"), 1, 2023).splitlines()


words_to_digit_map = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

INF = int(1e9)


def part1():
    data = get_data()

    ans = 0

    for line in data:
        temp = [i for i in line if i.isdigit()]
        ans += int(f"{temp[0]}{temp[-1]}")

    return ans


def part2():
    data = get_data()

    ans = 0

    for line in data:
        start_idx = INF
        st1 = "0"
        end_idx = -INF
        st2 = "0"

        for k, v in words_to_digit_map.items():
            early_find = line.find(k)
            greedy_find = line.rfind(k)

            if early_find == -1 or greedy_find == -1:
                continue

            if start_idx > early_find:
                start_idx = early_find
                st1 = v

            if end_idx < greedy_find:
                end_idx = greedy_find
                st2 = v

        if end_idx == -1:
            st2 = st1

        digit_str = f"{st1}{st2}"

        # print(line[:-1], digit_str)
        ans += int(digit_str)

    return ans


if __name__ == "__main__":
    p1 = part1()
    p2 = part2()

    print(f"Par1: {p1}, Part2: {p2}")
