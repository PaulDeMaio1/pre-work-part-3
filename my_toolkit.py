def calculate_average(numbers):
    """Will return the average of a list of numbers, or 0 if the list is empty."""
    if len(numbers) == 0:
        return 0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def find_max_and_min(numbers):
    """Will return (max_value, min_value) using a manual loop.

    Returns (None, None) if the list is empty.
    """
    if len(numbers) == 0:
        return (None, None)
    max_value = numbers[0]
    min_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
    return (max_value, min_value)


def count_occurrences(items, target):
    total = 0
    for item in items:
        if item == target:
            total += 1
    return total


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def create_report(title, scores):
    """Will return a formated report string with the title, number of scores, average, highest, and lowest score."""
    average = calculate_average(scores)
    max_value, min_value = find_max_and_min(scores)

    lines = [
        "=" * 30,
        title.center(30),
        "=" * 30,
        f"Number of scores: {len(scores)}",
        f"Average: {average:.2f}",
        f"Highest: {max_value}",
        f"Lowest: {min_value}",
        "=" * 30,
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    # Will be testing the functions below
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    print()
    print("--- Edge cases ---")

    print(f"Average of []: {calculate_average([])}  (expected 0)")
    print(f"Max/Min of []: {find_max_and_min([])}  (expected (None, None))")
    print()

    print(f"Max/Min of [7]: {find_max_and_min([7])}  (expected (7, 7))")
    print(f"Max/Min of [-5, -1, -10]: {find_max_and_min([-5, -1, -10])}  (expected (-1, -10))")
    print(f"Average of [-5, 5]: {calculate_average([-5, 5])}  (expected 0.0)")
    print()

    print(f"Count of 3 in [3, 1, 3, 3, 2]: {count_occurrences([3, 1, 3, 3, 2], 3)}  (expected 3)")
    print(f"Count of 99 in test_scores: {count_occurrences(test_scores, 99)}  (expected 0)")
    print(f"Count of 'a' in []: {count_occurrences([], 'a')}  (expected 0)")
    print(f"Count of 'a' in ['a', 'b', 'a']: {count_occurrences(['a', 'b', 'a'], 'a')}  (expected 2)")
    print()

    print(f"'A man a plan a canal Panama': {is_palindrome('A man a plan a canal Panama')}  (expected True)")
    print(f"'a': {is_palindrome('a')}  (expected True)")
    print(f"'RaceCar': {is_palindrome('RaceCar')}  (expected True)")
    print(f"'': {is_palindrome('')}  (expected True)")
    print(f"'Hello World': {is_palindrome('Hello World')}  (expected False)")
    print()

    print(create_report("Empty Class", []))
    print()
    print(create_report("Solo Student", [100]))