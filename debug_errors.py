
def calculate_average(score_list):
    """Calculate the average score.

Return None if the average cannot be calculated.
"""
    try:
        total_score = sum(score_list)
        number_of_scores = len(score_list)
        return total_score / number_of_scores
    except ZeroDivisionError:
        print("Oops! An empty list has no average.")
        return None
    except TypeError:
        print("Please provide a list containing numbers.")
        return None


def get_list_element(item_list, position):
    """Get an item from a list and handle invalid input safely."""
    try:
        return item_list[position]
    except IndexError:
        print("That position is outside the list.")
        return None
    except TypeError:
        print("Invalid input: check the list and position types.")
        return None


# Test average calculation
quiz_scores = [78, 85, 92, 67]
print("Average quiz score:", calculate_average(quiz_scores))

empty_scores = []
print("Average of empty scores:", calculate_average(empty_scores))

# Test list element retrieval
fruit_basket = ["mango", "orange", "grapes"]

print("Selected fruit:", get_list_element(fruit_basket, 2))
print("Selected fruit:", get_list_element(fruit_basket, 8))
print("Selected fruit:", get_list_element(None, 1))
