class FactorialCalculator:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

if __name__ == "__main__":
    calc = FactorialCalculator()
    print(calc.factorial(5))  # Example Run: factorial of 5
