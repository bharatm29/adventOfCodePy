def get_data():
    with open("input.txt", "r") as f:
        return f.read().split("\n")


def part1(data):
    loc_dict = {}

    instruction = data[0]

    for line in data[2:]:
        pos, _, dirs = line.strip().partition(" = ")
        left, right = dirs[1:-1].split(", ")

        loc_dict[pos] = (left, right)

    ans = 0
    inst_index = 0

    cur_pos = 'AAA'

    while cur_pos != 'ZZZ':
        inst = instruction[inst_index]

        if inst == 'R':
            cur_pos = loc_dict[cur_pos][1]
        else:
            cur_pos = loc_dict[cur_pos][0]

        ans += 1

        inst_index += 1
        if inst_index == len(instruction):
            inst_index = 0

    return ans


def find_steps(cur_pos, instruction, loc_dict):
    ans = 0
    inst_index = 0
    while cur_pos != 'ZZZ':
        inst = instruction[inst_index]

        if inst == 'R':
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
    starting_pos = []

    instruction = data[0]

    for line in data[2:]:
        pos, _, dirs = line.strip().partition(" = ")
        left, right = dirs[1:-1].split(", ")

        loc_dict[pos] = (left, right)

        if pos[-1] == '1':
            starting_pos.append(pos)

    ans = int(1e9)


if __name__ == '__main__':
    file_data = get_data()
    p1 = part1(file_data)
    p2 = part2(file_data)
    print(f"Part1: {p1}, Part2: {p2}")
