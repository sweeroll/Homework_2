from typing import List


def calculate(grid: List[List]) -> int:
    """Поиск островов."""
    if not grid:
        return 0

    def f(y: int, x: int) -> None:
        """Поиск соседних единиц."""
        grid[y][x] = 0
        if x > 0 and grid[y][x - 1] == 1:
            f(y, x - 1)
        if x < len(grid[0]) - 1 and grid[y][x + 1] == 1:
            f(y, x + 1)
        if y > 0 and grid[y - 1][x] == 1:
            f(y - 1, x)
        if y < len(grid) - 1 and grid[y + 1][x] == 1:
            f(y + 1, x)

    number = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                number += 1
                f(y, x)
    return number
