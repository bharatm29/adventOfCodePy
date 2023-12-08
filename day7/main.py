from collections import Counter


def get_data():
    with open("input.txt", "r") as f:
        return f.read().split("\n")


def get_numeric(n: str):
    if n.isdigit():
        return int(n)

    return {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[n]


def get_strength(hand):
    strength = tuple(sorted(Counter(hand).values(), reverse=True))
    return strength, hand


def part1(data: list[str]):
    hands = []
    for line in data:
        hand, bid = line.split()
        hands.append((tuple(get_numeric(i) for i in hand), int(bid)))

    print(hands)

    hands.sort(key=lambda x: get_strength(x[0]))

    ans = 0

    for i, hand_data in enumerate(hands):
        bid = hand_data[1]
        ans += ((i + 1) * bid)

    return ans


if __name__ == '__main__':
    file_data = get_data()
    print(file_data)
    p1 = part1(file_data)
    print(f"Part1: {p1}")
