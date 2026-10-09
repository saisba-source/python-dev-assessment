
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

# Create three book instances
book1 = Book(
    "Harry Potter and the Philosopher's Stone",
    "J.K. Rowling",
    "9780747532699",
    1997,
)

book2 = Book(
    "The Alchemist",
    "Paulo Coelho",
    "9780061122415",
    1988,
)

book3 = Book(
    "A Man Called Ove",
    "Fredrik Backman",
    "9781476738024",
    2012,
)
for book in [book1, book2, book3]:
    print(book.get_summary())
    print(f"Age: {book.get_age()} years")
    print()