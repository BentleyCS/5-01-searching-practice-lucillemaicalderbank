import random

def randomSearch(items: list, target) -> int:
    tries = 0
    while True:
        tries += 1
        index = random.randint(0, len(items) - 1)
        if items[index] == target:
            print(f"Random search found the target after {tries} tries.")
            return index

def linearSearch(items: list, target) -> tuple[int, int]:
    checks = 0
    for i, value in enumerate(items):
        checks += 1
        if value == target:
            return i, checks
    return -1, checks

def binarySearch(items: list, target) -> tuple[int, int]:
    left, right = 0, len(items) - 1
    checks = 0
    while left <= right:
        checks += 1
        mid = (left + right) // 2
        if items[mid] == target:
            return mid, checks
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, checks