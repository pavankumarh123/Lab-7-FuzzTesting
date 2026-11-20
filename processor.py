
def parse_int_list(data):
    """Convert comma-separated values into a list of integers."""
    if not isinstance(data, str):
        raise TypeError("Input must be a string")

    if not data.strip():
        return []

    try:
        return [int(item.strip()) for item in data.split(",")]
    except ValueError:
        raise ValueError("Input must contain only integers")


def sanitize_string(value):
    """Remove unwanted special characters from a string."""
    if not isinstance(value, str):
        raise TypeError("Input must be a string")

    return "".join(
        char for char in value
        if char.isalnum() or char.isspace()
    )


def safe_average(numbers):
    """Calculate the average of a list of numbers."""
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not numbers:
        return 0

    if any(
        isinstance(n, bool) or not isinstance(n, (int, float))
        for n in numbers
    ):
        raise ValueError("All elements must be numbers")

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print("LAB 7 - FUZZ TESTING")
    print("--------------------")

    print("Function 1:", parse_int_list("10,20,30"))
    print("Function 2:", sanitize_string("Hello@123!"))
    print("Function 3:", safe_average([10, 20, 30]))

    print("\nApplication executed successfully.")
