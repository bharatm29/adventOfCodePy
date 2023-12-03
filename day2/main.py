import unittest


class Day2Test(unittest.TestCase):
    """ For testing with small input """

    def test_small_case_part1(self):
        self.assertEqual(part1(day2_data), 8)

    def test_small_case_part2(self):
        self.assertEqual(part2(day2_data), 2286)


def get_data():
    with open("input.txt", "r") as f:
        return f.read().split("\n")


day2_data: list[str] = get_data()

RED = 0
BLUE = 1
GREEN = 2

Balls = list[tuple[int, int, int]]


class GameData:
    def __init__(self, number: int, ball_sets: Balls):
        self.number = number
        self.ball_sets = ball_sets


def convert_to_ball_sets(game_sets):
    ls: Balls = []

    for game_set in game_sets:
        ball_set = game_set.strip().split(", ")
        red, blue, green = 0, 0, 0

        for balls_str in ball_set:
            balls = balls_str.strip().split()

            ball_amount = int(balls[0])
            ball_color = balls[1]

            if ball_color == "red":
                red = ball_amount
            elif ball_color == "blue":
                blue = ball_amount
            else:
                green = ball_amount

        ls.append((red, blue, green))

    return ls


def transform_data(line: str):
    semi_colon_pos = line.find(":")
    game_number = int(line[5:semi_colon_pos])

    game_sets = line[semi_colon_pos + 2:].split(";")

    ball_sets = convert_to_ball_sets(game_sets)

    return GameData(game_number, ball_sets)


def plausible(game_data: GameData):
    max_red = 12
    max_green = 13
    max_blue = 14

    for balls in game_data.ball_sets:
        red = balls[RED]
        green = balls[GREEN]
        blue = balls[BLUE]

        if red > max_red or blue > max_blue or green > max_green:
            return False

    return True


def part1(data):
    ans = 0

    for line in data:
        game_data = transform_data(line)

        if plausible(game_data):
            ans += game_data.number

    return ans


def mim_needed_ball_power(ball_sets: Balls):
    mx_green, mx_red, mx_blue = -1, -1, -1

    for balls in ball_sets:
        mx_red = max(balls[RED], mx_red)
        mx_green = max(balls[GREEN], mx_green)
        mx_blue = max(balls[BLUE], mx_blue)

    return mx_red * mx_green * mx_blue


def part2(data):
    ans = 0

    for line in data:
        game_data = transform_data(line)

        ans += mim_needed_ball_power(game_data.ball_sets)

    return ans


if __name__ == '__main__':
    p1 = part1(day2_data)
    p2 = part2(day2_data)
    print(f"Part1: {p1}, Part2: {p2}")

    # unittest.main()
