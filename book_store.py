
class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        """Return the book's age using 2026 as the current year."""
        return 2026 - self.publication_year

    def get_summary(self):
        """Return a short summary of the book."""
        return (
            f"'{self.title}' by {self.author}, "
            f"published in {self.publication_year}, "
            f"ISBN: {self.isbn}"
        )


# Create three book instances
book1 = Book(
    "The Hobbit",
    "J.R.R. Tolkien",
    "9780547928227",
    1937,
)

book2 = Book(
    "The Secret Garden",
    "Frances Hodgson Burnett",
    "9780141321068",
    1911,
)

book3 = Book(
    "Wonder",
    "R.J. Palacio",
    "9780375869020",
    2012,
)


# Display each book's summary and age
for book in [book1, book2, book3]:
    print(book.get_summary())
    print(f"Age: {book.get_age()} years")
    print()
