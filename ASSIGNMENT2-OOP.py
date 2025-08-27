# Base class and subclasses demonstrating polymorphism
class Vehicle:
    def move(self):
        """Generic move method (to be overridden by subclasses)."""
        pass


# Subclasses with their own move() implementations
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Goat(Vehicle):
    def move(self):
        print("Walking 🐐")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")


# --- Testing Polymorphism ---
vehicles = [Car(), Plane(), Goat(), Bicycle()]

for v in vehicles:
    v.move()  # Each object calls its own version of move()
