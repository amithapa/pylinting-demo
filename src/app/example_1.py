import logging
from typing import List


def is_unique(s: str) -> int:
    s_list: List[str] = list(s)
    print(s_list)
    s_list.sort()

    for i in range(len(s_list) - 1):
        if s_list[i] == s_list[i + 1]:
            return 0
    else:
        return 1


if __name__ == "__main__":
    print(is_unique(input()))
