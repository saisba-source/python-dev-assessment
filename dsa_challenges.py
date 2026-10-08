
def filter_and_sort_evens(numbers):
    """Return all even numbers from the list in ascending order."""
    even_numbers = [number for number in numbers if number % 2 == 0]
    return sorted(even_numbers)


def count_character_frequency(text):
    """Return a dictionary counting each character in the text."""
    frequency = {}

    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    return frequency


# Test 1: Filter and sort even numbers
numbers = [5, 2, 8, 1, 4]
print(filter_and_sort_evens(numbers))


# Test 2: Count character frequency
text = "hello"
print(count_character_frequency(text))
