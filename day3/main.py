import unittest


class Test(unittest.TestCase):
    def test_small_input_part1(self):
        self.assertEqual(part1(data_set), 4361)

    def test_small_input_part2(self):
        self.assertEqual(part2(data_set), 467835)


def get_data():
    with open("input.txt", "r") as f:
        return f.read().split("\n")


data_set = get_data()


class Token:
    def __init__(self, val: int, start_index: int, end_index: int, line_no: int):
        self.val = val
        self.start_index = start_index
        self.end_index = end_index
        self.line_no = line_no

    def __str__(self):
        return f"Token( {self.val}, from {self.start_index} to {self.end_index} at line {self.line_no} )"

    def __repr__(self):
        return f"Token( {self.val}, from {self.start_index} to {self.end_index} at line {self.line_no} )"


def tokenize_line(string: str, line_no: int, symbol_index):
    length = len(string)
    curr = 0

    tokens = []

    while curr < length:
        curr_char = string[curr]
        if curr_char == ".":
            curr += 1
            continue

        if curr_char.isdigit():
            pos = curr

            while curr < length and string[curr].isdigit():
                curr += 1

            tokens.append(Token(int(string[pos:curr]), pos, curr - 1, line_no))
        else:
            curr_index = line_no * length + curr
            symbol_index.append(curr_index)

            if curr_char == "*":  # adding gear to dictionary for part2
                gears[curr_index] = []

            curr += 1

    return tokens


def is_near_symbol(token: Token, symbol_index: list[int], size: int, data: list[str]) -> bool:
    dirs: list[tuple[int, int]] = [
        (-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)
    ]

    flag = False

    for idx in range(token.start_index, token.end_index + 1):
        for d in dirs:
            new_line_no = (token.line_no - d[1])
            new_pos = (idx + d[0])
            new_idx = new_line_no * size + new_pos

            if new_idx in symbol_index:
                if data[new_line_no][new_pos] == "*":
                    if token not in gears[new_idx]:
                        gears[new_idx].append(token)
                flag = True

    return flag


def part1(data):
    line_tokens = []
    symbol_index = []

    for line_no, line in enumerate(data):
        line_tokens.append(tokenize_line(line, line_no, symbol_index))

    ans = 0

    for line_data in line_tokens:
        for token in line_data:
            if is_near_symbol(token, symbol_index, len(data[0]), data):
                ans += token.val

    return ans


gears: dict[int, list[Token]] = {}


def part2(data):
    line_tokens = []
    symbol_index = []

    for line_no, line in enumerate(data):
        line_tokens.append(tokenize_line(line, line_no, symbol_index))

    ans = 0

    for line_data in line_tokens:
        for token in line_data:
            is_near_symbol(token, symbol_index, len(data[0]), data)

    for gear_index, near_tokens in gears.items():
        if len(near_tokens) != 2:
            continue

        ans += near_tokens[0].val * near_tokens[1].val

    return ans


if __name__ == '__main__':
    p1 = part1(data_set)
    p2 = part2(data_set)
    print(f"Part1: {p1}, Part2: {p2}")
