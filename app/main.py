from app.models import Book
from app.serializers import BookJsonSerializer, BookXmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializers = {
        "json": BookJsonSerializer,
        "xml": BookXmlSerializer,
    }

    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if serializer is None:
                raise ValueError(f"Unknown serializer type: {method_type}")

            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
