def get_data():
    with open("input.txt", "r") as f:
        return f.read().split("\n")[:-1]


def add_last(nums: list[int]) -> int:
    last = nums[-1]

    for n in reversed(nums[:-1]):
        last += n

    return last


def add_first(nums: list[int]) -> int:
    first = nums[-1]

    for n in reversed(nums[:-1]):
        first = n - first

    return first


def convert_to_diff_list(nums: list[int]) -> list[int]:
    n = len(nums)

    new_nums = []

    for i in range(n - 1):
        new_nums.append(nums[i + 1] - nums[i])

    return new_nums


def convert_to_series(nums: list[int], last=True) -> int:
    def check_zero(nums) -> bool:
        for i in nums:
            if i != 0:
                return False
        return True

    lasts = []
    firsts = []

    ls = nums
    lasts.append(ls[-1])
    firsts.append(ls[0])

    while not check_zero(ls):
        ls = convert_to_diff_list(ls)
        lasts.append(ls[-1])
        firsts.append(ls[0])

    return add_last(lasts) if last else add_first(firsts)


def part1(data: list[str]):
    ans = 0

    for line in data:
        nums = [int(i) for i in line.split()]
        ans += convert_to_series(nums)

    return ans


def part2(data: list[str]):
    ans = 0

    for line in data:
        nums = [int(i) for i in line.split()]
        ans += convert_to_series(nums, last=False)

    return ans


if __name__ == "__main__":
    file_data = get_data()
    p1 = part1(file_data)
    print(f"Part1: {p1}")

    p2 = part2(file_data)
    print(f"Part2: {p2}")
