class Treatment:
    def __init__(self, date, description):
        self.__date = date
        self.__description = description

    def get_date(self):
        return self.__date

    def get_description(self):
        return self.__description

    def display_details(self):
        print(f"Date: {self.__date}, Description: {self.__description}")

class Animal:
    def __init__(self, name, species, age):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__treatments = []

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def add_treatment(self, treatment):
        self.__treatments.append(treatment)

    def get_treatments(self):
        return self.__treatments

    def display_info(self):
        print(f"Name: {self.__name}, Species: {self.__species}, Age: {self.__age}")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.__breed}")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, "Cat", age)
        self.__color = color

    def get_color(self):
        return self.__color

    def display_info(self):
        super().display_info()
        print(f"Color: {self.__color}")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, "Bird", age)
        self.__wing_span = wing_span

    def get_wing_span(self):
        return self.__wing_span

    def display_info(self):
        super().display_info()
        print(f"Wing Span: {self.__wing_span} cm")

# Example usage:
animals = []
while True:
    print("\nEnter the details for an animal (or 'q' to quit):")
    name = input("Name: ")
    if name.lower() == "q":
        break
    species = input("Species: ").lower()
    age = int(input("Age: "))
    if species == "dog":
        breed = input("Breed: ")
        animal = Dog(name, age, breed)
    elif species == "cat":
        color = input("Color: ")
        animal = Cat(name, age, color)
    elif species == "bird":
        wing_span = int(input("Wing Span (in cm): "))
        animal = Bird(name, age, wing_span)
    else:
        print("Unknown species. Please try again.")
        continue
    animals.append(animal)

print("\nAnimal details:")
for animal in animals:
    animal.display_info()

# Add treatments
for animal in animals:
    while True:
        add_treatment = input(f"\nAdd a treatment for {animal.get_name()}? (y/n): ").lower()
        if add_treatment == 'n':
            break
        date = input("Treatment Date: ")
        description = input("Treatment Description: ")
        treatment = Treatment(date, description)
        animal.add_treatment(treatment)

# Display treatments
for animal in animals:
    print(f"\nTreatments for {animal.get_name()}:")
    treatments = animal.get_treatments()
    if treatments:
        for treatment in treatments:
            treatment.display_details()
    else:
        print("No treatments recorded.")
