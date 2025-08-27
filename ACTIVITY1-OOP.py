# Base Class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title       # Public attribute
        self.author = author     # Public attribute
        self.__pages = pages               # Private attribute (encapsulation)
        self.__current_page = 0          # Track reading progress

    def read(self, pages):
        """Simulate reading pages from the book."""
        if self.__current_page + pages <= self.__pages:
            self.__current_page += pages
            print(f"You read {pages} pages of '{self.title}'. Now on page {self.__current_page}.")
        else:
            self.__current_page = self.__pages
            print(f"You finished reading '{self.title}' ")

    def get_progress(self):
        """Getter method for reading progress."""
        return f"Progress: {self.__current_page}/{self.__pages} pages read."

    def get_pages(self):
        """Getter for total pages (encapsulation)."""
        return self.__pages


# Derived Class: EBook (Inheritance + Polymorphism)
class EBook(Book):
    def __init__(self, title, author, pages, file_size_mb):
        super().__init__(title, author, pages)
        self.file_size_mb = file_size_mb   # Unique attribute for EBook

    def read(self, pages):
        """Override read(): EBooks allow bookmarking automatically."""
        print(f"Opening eBook '{self.title}' on your device...")
        super().read(pages)
        print(f"Bookmark saved at current page.")


# Derived Class: AudioBook (Inheritance + Polymorphism)
class AudioBook(Book):
    def __init__(self, title, author, pages, narrator):
        super().__init__(title, author, pages)
        self.narrator = narrator  # Unique attribute for AudioBook

    def read(self, minutes):
        """Override read(): AudioBooks are 'listened' to in minutes instead of pages."""
        print(f"Listening to '{self.title}' narrated by {self.narrator} for {minutes} minutes.")
        # For simplicity, assume 1 min = 1 page
        super().read(minutes)


# --- Testing the classes ---

# Regular book
book1 = Book("One Eye General", "Elly Tumwine", 328)
book1.read(50)
print(book1.get_progress())

print("\n---\n")

# EBook
ebook1 = EBook("Sowing the Mastered Seed", "Yoweri Kaguta Museveni", 75, file_size_mb=5)
ebook1.read(40)
print(ebook1.get_progress())

print("\n---\n")

# AudioBook
audiobook1 = AudioBook("Home coming", "Obulejo Ivan", 400, narrator="Obulejo Ivan")
audiobook1.read(30)
print(audiobook1.get_progress())
