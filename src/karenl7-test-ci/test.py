class Test:
    def __init__(self):
        self.x = 1
        self.y = 2

    def __str__(self):
        return f"Test(x={self.x}, y={self.y})"

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

# Create an instance of Test
test_instance = Test()

# Print the instance to see the output
print(test_instance)