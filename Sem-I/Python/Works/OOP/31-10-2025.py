class calc:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        self.result = a / b
        return self.result

a = calc()
print("Addition:", a.add(10, 5))
print("Subtraction:",a.subtract(10, 5))
print("Multiplication:", a.multiply(10, 5))
print("Division:", a.divide(10, 5))


class calc:
    def __init__(self):
        self.result = 0
        self.a=0
        self.b=0

    def add(self):
        self.result = self.a + self.b
        return self.result

    def subtract(self):
        self.result = self.a - self.b
        return self.result

    def multiply(self):
        self.result = a * b
        return self.result

    def divide(self):
        self.result = self.a / self.b
        return self.result

a = calc()

print("Addition:", a.add(10, 5))
print("Subtraction:",a.subtract(10, 5))
print("Multiplication:", a.multiply(10, 5))
print("Division:", a.divide(10, 5))

      