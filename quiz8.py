class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Example usage
sum = Calculator.add(1000, 12220)
print(f"The sum is: {sum}")
print(f"The count of add() calls: {Calculator.count}")