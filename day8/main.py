def get_data():
    with open("input.txt", "r") as f:
        return f.read().split("\n")


def part1(data):
    loc_dict = {}

    instruction = data[0]

    for line in data[2:-1]:
        pos, _, dirs = line.strip().partition(" = ")
        left, right = dirs[1:-1].split(", ")

        loc_dict[pos] = (left, right)

    return find_loop_size("AAA", instruction, loc_dict)


def gcd(a: int, b: int):
    while b != 0:
        R = a % b
        a = b
        b = R

    return a


def lcm(index: int, ls: list[int]) -> int:
    if index == 0:
        return ls[0]

    a: int = ls[index]

    b: int = lcm(index - 1, ls)

    return (a * b) // (gcd(a, b))


def find_loop_size(cur_pos, instruction, loc_dict):
    ans = 0
    inst_index = 0

    while not cur_pos.endswith("Z"):
        inst = instruction[inst_index]

        if inst == "R":
            cur_pos = loc_dict[cur_pos][1]
        else:
            cur_pos = loc_dict[cur_pos][0]

        ans += 1

        inst_index += 1
        if inst_index == len(instruction):
            inst_index = 0

    return ans


def part2(data):
    loc_dict = {}

    instruction = data[0]

    positions = []

    for line in data[2:-1]:
        pos, _, dirs = line.strip().partition(" = ")
        left, right = dirs[1:-1].split(", ")

        loc_dict[pos] = (left, right)

        if pos.endswith('A'):
            positions.append(pos)


    loop_sizes = []

    for pos in positions:
        sz = find_loop_size(pos, instruction, loc_dict)
        loop_sizes.append(sz)

    return lcm(len(loop_sizes) - 1, loop_sizes)


if __name__ == "__main__":
    file_data = get_data()
    p1 = part1(file_data)
    print(f"Part1: {p1}, ", end="")

    p2 = part2(file_data)
    print(f"Part2: {p2}")
