class Item:
    def __init__(self, title, author_director, publication_release_year):
        self.title = title
        self.author_director = author_director
        self.publication_release_year = publication_release_year
        self.__is_available = True

    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        else:
            return False

    def return_item(self):
        self.__is_available = True


class Book(Item):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre


class Audiobook(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year, genre)


class Movie(Item):
    def __init__(self, title, director, release_year, runtime):
        super().__init__(title, director, release_year)
        self.runtime = runtime


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def search(self, title):
        return [item for item in self.items if item.title.lower() == title.lower()]

    def check_availability(self, title):
        search_results = self.search(title)
        if not search_results:
            return f"No items found with title: {title}"
        return {item.title: item.is_available() for item in search_results}

    def borrow_item(self, title):
        search_results = self.search(title)
        if not search_results:
            return f"No items found with title: {title}"
        for item in search_results:
            if item.is_available():
                item.borrow()
                return f"You have borrowed '{title}'"
        return f"'{title}' is currently not available"

    def return_item(self, title):
        search_results = self.search(title)
        if not search_results:
            return f"No items found with title: {title}"
        for item in search_results:
            if not item.is_available():
                item.return_item()
                return f"You have returned '{title}'"
        return f"'{title}' was not borrowed"


# Example usage
library = Library()

# Adding items to the library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
audiobook1 = Audiobook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
movie1 = Movie("Inception", "Christopher Nolan", 2010, 148)

library.add_item(book1)
library.add_item(audiobook1)
library.add_item(movie1)

# Searching for items
print(library.search("The Great Gatsby"))

# Checking availability
print(library.check_availability("The Great Gatsby"))

# Borrowing an item
print(library.borrow_item("The Great Gatsby"))





# Checking availability again
print(library.check_availability("The Great Gatsby"))

# Returning an item
print(library.return_item("The Great Gatsby"))

# Checking availability after returning
print(library.check_availability("The Great Gatsby")) 












from datetime import date

class Treatment:
    def __init__(self, treatment_date, description):
        self.treatment_date = treatment_date
        self.description = description

    def display_details(self):
        return f"Date: {self.treatment_date}, Description: {self.description}"


class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.__treatments = []

    def add_treatment(self, treatment):
        self.__treatments.append(treatment)

    def get_treatments(self):
        return self.__treatments

    def display_info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Breed: {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, "Cat", age)
        self.color = color

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Color: {self.color}"


class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, species, age)

    def display_info(self):
        base_info = super().display_info()
        return base_info


class VeterinaryClinic:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def record_treatment(self, animal_name, treatment):
        animal = self.search_animal_by_name(animal_name)
        if animal:
            animal.add_treatment(treatment)
            return f"Treatment recorded for {animal_name}"
        else:
            return f"Animal named {animal_name} not found"

    def search_animal_by_name(self, name):
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                return animal
        return None

    def search_animals_by_species(self, species):
        return [animal for animal in self.animals if animal.species.lower() == species.lower()]

    def display_animal_info(self, name):
        animal = self.search_animal_by_name(name)
        if animal:
            info = animal.display_info()
            treatments = "\n".join([t.display_details() for t in animal.get_treatments()])
            return f"{info}\nTreatments for {animal.name}:\n{treatments if treatments else 'No treatments recorded'}"
        else:
            return f"Animal named {name} not found"


# Example usage
clinic = VeterinaryClinic()

# Adding animals
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Tabby")
bird = Bird("Tweety", 1, "Canary")

clinic.add_animal(dog)
clinic.add_animal(cat)
clinic.add_animal(bird)

# Recording treatments
treatment1 = Treatment(date(2024, 5, 13), "Vaccination")
treatment2 = Treatment(date(2024, 5, 20), "Checkup")

clinic.record_treatment("Buddy", treatment1)
clinic.record_treatment("Whiskers", treatment2)

# Displaying animal info
print(clinic.display_animal_info("Buddy"))
print(clinic.display_animal_info("Whiskers"))
print(clinic.display_animal_info("Tweety"))

# Searching for animals by species
print([animal.display_info() for animal in clinic.search_animals_by_species("Dog")])
print([animal.display_info() for animal in clinic.search_animals_by_species("Cat")])
print([animal.display_info() for animal in clinic.search_animals_by_species("Bird")])
