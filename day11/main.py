import os
import aocd

def get_data():
    # return aocd.get_data(os.getenv("AOC"), 11, 2023).split("\n")
    with open("input.txt", "r") as f:
        return f.read().split("\n")[:-1]


def transform_matrix(data: list[str]) -> list[list[str]]:
    matrix: list[list[str]] = []

    for line in data:
        matrix.append(list(line))

    expanded_row_matrix: list[list[str]] = []

    # expanding row
    for _, row in enumerate(matrix):
        expanded_row_matrix.append(row.copy())

        if "#" not in row:
            expanded_row_matrix.append(row.copy())

    expanded_column_matrix: list[list[str]] = []

    # expanding coloumn
    columns = []
    counter = 0
    for j in range(len(expanded_row_matrix[0])):
        if "#" not in [
            expanded_row_matrix[i][j] for i in range(len(expanded_row_matrix))
        ]:
            columns.append(j + counter)
            counter += 1

    for _, row in enumerate(expanded_row_matrix):
        new_row = row.copy()
        for c in columns:
            new_row.insert(c, ".")
        expanded_column_matrix.append(new_row)

    return expanded_column_matrix


def validate_cords(cord: tuple[int, int], matrix: list[list[str]]) -> bool:
    return (
        cord[0] >= 0
        and cord[0] < len(matrix)
        and cord[1] >= 0
        and cord[1] < len(matrix[0])
    )


def walk(
    current: tuple[int, int], end: tuple[int, int], matrix: list[list[str]]
) -> int:
    q = []

    visited: list[tuple[int, int]] = []

    q.append((current, 0))
    visited.append(current)

    while q:
        ((x, y), steps) = q.pop()

        if (x, y) == end:
            return steps

        for x1, y1 in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_x = x1 + x
            new_y = y1 + y

            if validate_cords((new_x, new_y), matrix) and (new_x, new_y) not in visited:
                visited.append((new_x, new_y))

                q.append(((new_x, new_y), steps + 1))

                q.sort(key=lambda z: z[1], reverse=True)

    return -1


def part1(data: list[str]):
    matrix = transform_matrix(data)

    cords: dict[int, tuple[int, int]] = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                cords[len(cords)] = (i, j)

    ans = 0

    for i in range(len(cords)):
        for j in range(i, len(cords)):
            ans += abs(cords[i][0] - cords[j][0]) + abs(cords[i][1] - cords[j][1])

    return ans


if __name__ == "__main__":
    file_data = get_data()

    p1 = part1(file_data)
    print(f"Part1: {p1}")

    # p2 = part2(file_data)
    # print("Part2: {p2}")

# [1, 2, 3, 4] => 2(5), 3(6)
# [1, 2, 5, 3, 6, 4]
