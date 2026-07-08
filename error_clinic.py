# Error Code Clinic
# Name: Victoria

# Snippet 1
# Error that would happen: ZeroDivisionError
# Why: The original code tried to divide 10 by 0.
# Fix: Check if y is 0 before dividing.
x = 10
y = 0

if y != 0:
    result = x / y
    print("Snippet 1 Result:", result)
else:
    print("Snippet 1: Cannot divide by zero")


# Snippet 2
# Error that would happen: IndexError
# Why: The original code used numbers[i + 1], which goes past the end of the list.
# Fix: Use numbers[i] instead.
numbers = [1, 2, 3, 4, 5]

print("Snippet 2:")
for i in range(len(numbers)):
    print(numbers[i])


# Snippet 3
# Error that would happen: SyntaxError
# Why: The original function line was missing a colon.
# Fix: Add : after def calculate_area(radius).
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print("Snippet 3:", calculate_area(radius))


# Snippet 4
# Error that would happen: SyntaxError
# Why: The if and else lines were missing colons.
# Fix: Add : after if and else.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print("Snippet 4:", is_even(4))
print("Snippet 4:", is_even(7))


# Snippet 5
# Error that would happen: SyntaxError
# Why: The for loop line was missing a colon.
# Fix: Add : after range(5).
print("Snippet 5:")
for i in range(5):
    print(i)


# Snippet 6
# Error that would happen: SyntaxError
# Why: The original code tried to put two strings together without +.
# Fix: Use + to join "Hello, " and name.
def greet(name):
    return "Hello, " + name

print("Snippet 6:", greet("Alice"))


# Snippet 7
# Error that would happen: Logic error
# Why: The print statement was inside the loop, so it printed the total too many times.
# Fix: Put print after the loop finishes.
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print("Snippet 7: Sum of numbers:", total)

# Snippet 8
# Error that would happen: RecursionError / infinite recursion
# Why: The original code used factorial(n + 1), so n got bigger and never reached 0.
# Fix: Use factorial(n - 1) so n moves toward 0.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Snippet 8:", factorial(5))


# Snippet 9
# Error that would happen: Logic error
# Why: name == "Alice" or "Bob" is always True because "Bob" counts as true.
# Fix: Compare name to both values.
name = "Charlie"

if name == "Alice" or name == "Bob":
    print("Snippet 9: Hello, " + name)
else:
    print("Snippet 9: Hello, stranger!")


# Snippet 10
# Error that would happen: ZeroDivisionError
# Why: The original function divided by y when y was 0.
# Fix: Check if y is 0 before dividing.
def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

num1 = 10
num2 = 0

print("Snippet 10:", divide_numbers(num1, num2))