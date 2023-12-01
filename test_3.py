'''Function to sum the numbers in a time string.'''


def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS and returns the sum of the numbers
    separated by a colon. For example, 01:02:03 returns 6. Returns None if
    the time is not of the correct format."""

    list_of_nums = time_str.split(":")

    # Remove leading zeros
    for idx, num in enumerate(list_of_nums):
        if num[0] == '0':
            list_of_nums[idx] = num[1]

    # Check the time is in the correct format
    hour = int(list_of_nums[0])
    minute = int(list_of_nums[1])
    second = int(list_of_nums[2])
    if not 0 <= hour <= 23 or not 0 <= minute <= 59 \
            or not 0 <= second <= 59:
        return None

    # Sum the numbers
    return sum(int(num) for num in list_of_nums)
