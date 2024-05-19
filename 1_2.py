class Item:
    def __init__(self, title, author_director, publication_release_year):
        self.__title = title
        self.__author_director = author_director
        self.__publication_release_year = publication_release_year
        self.__is_available = True

    def get_title(self):
        return self.__title

    def get_author_director(self):
        return self.__author_director

    def get_publication_release_year(self):
        return self.__publication_release_year

    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            print(f"You have borrowed {self.__title}.")
        else:
            print(f"{self.__title} is currently not available.")

    def return_item(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"You have returned {self.__title}.")
        else:
            print(f"{self.__title} is already available.")


class Book(Item):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.__genre = genre

    def get_genre(self):
        return self.__genre


class Audiobook(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year, genre)


class Movie(Item):
    def __init__(self, title, director, release_year, runtime):
        super().__init__(title, director, release_year)
        self.__runtime = runtime

    def get_runtime(self):
        return self.__runtime


items = []
while True:
    print("\nEnter the details for an item (or 'q' to quit):")
    title = input("Title: ")
    if title.lower() == "q":
        break
    author_director = input("Author/Director: ")
    publication_release_year = int(input("Publication/Release year: "))
    item_type = input("Type (book, audiobook, movie): ").lower()
    if item_type == "book":
        genre = input("Genre: ")
        items.append(Book(title, author_director, publication_release_year, genre))
    elif item_type == "audiobook":
        genre = input("Genre: ")
        items.append(Audiobook(title, author_director, publication_release_year, genre))
    elif item_type == "movie":
        runtime = int(input("Runtime: "))
        items.append(Movie(title, author_director, publication_release_year, runtime))
    else:
        print("Invalid item type.")

print("\nItem details:")
for item in items:
    if isinstance(item, Book) or isinstance(item, Audiobook):
        print(item.get_title())
        print(item.get_genre())
    elif isinstance(item, Movie):
        print(item.get_title())
        print(item.get_runtime())

while True:
    action = input("\nEnter 'search', 'borrow', 'return', or 'quit': ").lower()
    if action == "search":
        title_to_search = input("Enter the title of the item to search: ")
        found = False
        for item in items:
            if item.get_title() == title_to_search:
                print(f"Found: {item.get_title()}")
                print(f"Type: {'book' if isinstance(item, Book) or isinstance(item, Audiobook) else 'movie'}")
                print(f"Author/Director: {item.get_author_director()}")
                print(f"Publication/Release year: {item.get_publication_release_year()}")
                if isinstance(item, Book) or isinstance(item, Audiobook):
                    print(f"Genre: {item.get_genre()}")
                elif isinstance(item, Movie):
                    print(f"Runtime: {item.get_runtime()}")
                found = True
                break
        if not found:
            print("Item not found.")

    elif action == "borrow":
        title_to_borrow = input("Enter the title of the item to borrow: ")
        for item in items:
            if item.get_title() == title_to_borrow and item.is_available():
                item.borrow()
                print(f"{title_to_borrow} has been borrowed.")
                break
        else:
            print("Item not found or already borrowed.")

    elif action == "return":
        title_to_return = input("Enter the title of the item to return: ")
        for item in items:
            if item.get_title() == title_to_return and not item.is_available():
                item.return_item()
                print(f"{title_to_return} has been returned.")
                break
        else:
            print("Item not found or not borrowed.")

    elif action == "quit":
        break

    else:
        print("Invalid action. Please try again.")