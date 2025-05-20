class Counter:
    # Class variable to keep track of the number of instances
    count = 0

    def __init__(self):
        # Increment the count each time a new object is created
        Counter.count += 1

    @classmethod
    def get_count(cls):
        # Return the number of instances created
        return cls.count

# Example usage
a = Counter()
b = Counter()
c = Counter()

print("Number of Counter instances created:", Counter.get_count())
