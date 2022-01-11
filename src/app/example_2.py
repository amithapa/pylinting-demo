"""
Example 2
"""


def generate() -> None:
    """
    Generate numbers
    """
    data = [2, 4, 6, 7, 32, 45, 67, 8]

    filtered_data = [
        num
        for num in [
            num for num in [num for num in data if num % 2 == 0] if num % 4 == 0
        ]
        if num % 2 == 0
    ]

    print(filtered_data)


generate()
