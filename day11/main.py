import os
import aocd


def get_data():
    return aocd.get_data(os.getenv("AOC"), 11, 2023).split("\n")
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
            x1 = cords[i][0]
            x2 = cords[j][0]
            y1 = cords[i][1]
            y2 = cords[j][1]

            ans += abs(x1 - x2) + abs(y1 - y2)

    return ans


def transform_matrix2(data: list[str]):
    matrix: list[list[str]] = []

    for line in data:
        matrix.append(list(line))

    empty_row = []
    empty_column = []

    for row_idx, row in enumerate(matrix):
        if "#" not in row:
            empty_row.append(row_idx)

    for j in range(len(matrix[0])):
        if "#" not in [matrix[i][j] for i in range(len(matrix))]:
            empty_column.append(j)
            pass

    return empty_column, empty_row


def part2(data, expansion_rate):
    matrix: list[list[str]] = []

    for line in data:
        matrix.append(list(line))

    empty_column, empty_row = transform_matrix2(data)

    print(empty_column, empty_row)

    cords: dict[int, tuple[int, int]] = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                cords[len(cords)] = (i, j)

    ans = 0

    for i in range(len(cords)):
        for j in range(i, len(cords)):
            x1 = cords[i][0]
            x2 = cords[j][0]
            y1 = cords[i][1]
            y2 = cords[j][1]

            ans += abs(x1 - x2) + abs(y1 - y2)

            for c in empty_row:
                if min(x1, x2) <= c <= max(x1, x2):
                    ans += int(expansion_rate - 1)

            for c in empty_column:
                if min(y1, y2) <= c <= max(y1, y2):
                    ans += int(expansion_rate - 1)

    return ans


if __name__ == "__main__":
    file_data = get_data()

    p1 = part1(file_data)
    print(f"Part1: {p1}")

    p2 = part2(file_data, expansion_rate=1e6)
    print(f"Part2: {p2}")
