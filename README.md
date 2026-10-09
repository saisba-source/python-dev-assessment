# Python Developer Assessment

This repository contains my Python Developer Assessment Bootcamp tasks. It covers Git and GitHub fundamentals, Python code style, data structures and algorithms, object-oriented programming, error handling, and API interaction.

## Tasks and Files

| Task | File | Description |
|---|---|---|
| 1.1 | `hello.py` | Prints a greeting message |
| 1.2 | `README.md` | Repository documentation and Git basics |
| 1.3 | `bad_style.py` | Code formatting and style checks using Black and Flake8 |
| 2.1 | `dsa_challenges.py` | Filters and sorts even numbers and counts character frequency |
| 2.2 | `book_store.py` | Defines a `Book` class with summary and age methods |
| 2.3 | `debug_errors.py` | Handles errors when calculating averages and retrieving list elements |
| 3.1 | `api_client.py` | Fetches sample user information from a REST API using Requests |

## Requirements

- Python 3.11
- Git
- `requests`
- `black`
- `flake8`

Install the required Python packages with:

```bash
py -3.11 -m pip install requests black flake8
```

## How to Run the Programs

Open a terminal in the project directory and run the relevant file:

```bash
py -3.11 hello.py
py -3.11 bad_style.py
py -3.11 dsa_challenges.py
py -3.11 book_store.py
py -3.11 debug_errors.py
py -3.11 api_client.py
```

The API task uses JSONPlaceholder at `https://jsonplaceholder.typicode.com/users` and requires an internet connection.

## Code Style Checks

Run Flake8 on an individual Python file:

```bash
py -3.11 -m flake8 dsa_challenges.py
```

Format a file using Black:

```bash
py -3.11 -m black bad_style.py
```

## Reflections

### Most Challenging Part

Learning Git branches, commits, merges, and pushing changes to GitHub was challenging at first. Working through each command step by step helped me understand the workflow and resolve the merge-message editor issue.

### Most Interesting Part

The API interaction task was interesting because it showed how Python can request data from a web service and display useful information.

### What I Learned

I practiced Python functions, list operations, dictionaries, classes, exception handling, HTTP requests, code formatting, and Git version control. I also learned to test my programs and check code style before committing changes.