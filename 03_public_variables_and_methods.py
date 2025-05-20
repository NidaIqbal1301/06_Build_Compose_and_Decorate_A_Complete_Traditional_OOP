class Car:
    # Public variable
    brand = ""

    # Public method
    def start(self):
        print(f"The {self.brand} car is starting.")

# Instantiate the class
my_car = Car()

# Access and set the public variable from outside the class
my_car.brand = "Toyota"

# Call the public method from outside the class
my_car.start()
