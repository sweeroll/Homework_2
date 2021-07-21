# публичные тестовые случаи из текста условия задачи
PUBLIC_TEST_CASES = [
    {"test_input": [[1, 0], [0, 0]], "expected": 1},
    {"test_input": [[1, 0], [1, 1]], "expected": 1},
    {"test_input": [[1, 0], [0, 1]], "expected": 2},
    {
        "test_input": [
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [1, 0, 1, 1, 0],
        ],
        "expected": 3,
    },
    {"test_input": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "expected": 0},
    {"test_input": [[1, 1, 1], [1, 1, 1], [1, 1, 1]], "expected": 1},
]

# Здесь можно написать свои тестовые случаи
SECRET_TEST_CASES = []