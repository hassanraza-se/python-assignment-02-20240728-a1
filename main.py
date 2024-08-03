# Hassan Raza -
# 1. Add Two Numbers with Strong Typing
def add_two_numbers():
    num1: int = int(input("Enter the first number: "))
    num2: int = int(input("Enter the second number: "))

    total_sum: int = num1 + num2

    print("The total sum is:", total_sum)


print('\n===== 1. Add Two Numbers ===== ')
add_two_numbers()


# 2. Agreement Boot
def favorite_animal():
    fav_animal: str = input("What's your favorite animal? ")

    print("My favorite animal is also", fav_animal + "!")


print('\n===== 2. Agreement Boot')
favorite_animal()


# 3. Fahrenheit to Celsius
def convert_temperature():
    degrees_fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))

    degrees_celsius: float = (degrees_fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")


print('\n===== 3. Fahrenheit to Celsius =====')
convert_temperature()


# 4. Triangle Perimeter with Strong Typing
def calculate_perimeter():
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    perimeter: float = side1 + side2 + side3

    print("The perimeter of the triangle is", perimeter)


print('\n===== 4. Triangle Perimeter =====')
calculate_perimeter()


# 5. Square Number
def square_number():
    number: float = float(input("Type a number to see its square: "))

    square: float = number * number

    print(f"{number} squared is {square}")


print('\n===== 5. Square Number =====')
square_number()


# 56. Delete a Number
def delete_a_number():
    numbers: list[int] = [1, 2, 3, 4, 5]

    numbers.remove(3)

    print("Modified list after removing 3:", numbers)


print('\n===== 6. Delete a Number =====')
delete_a_number()


# 7. Creating a List
def combine_lists():
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]

    list1.extend(list2)

    print("Combined list:", list1)


print('\n===== 7. Combine Lists =====')
combine_lists()


# 8. Pop Method
def use_pop_method():
    items: list[int] = [10, 20, 30, 40]

    removed_item: int = items.pop()

    print("Modified list:", items)
    print("Removed item:", removed_item)


print('\n===== 8. Use Pop Method =====')
use_pop_method()


# 9. Index Method
def find_index():
    colors: list[str] = ['red', 'blue', 'green', 'yellow']

    index_of_green: int = colors.index('green')

    print("The index of 'green' is", index_of_green)


print('\n===== 9. Find Index =====')
find_index()


# 10. Get Last Element
def get_last_element(lst: list):
    print("The last element is:", lst[-1])


print('\n===== 10. Get Last Element =====')
get_last_element([10, 20, 30, 40, 50])


# 11. Get a List
def get_user_list():
    values: list[str] = []

    while True:
        value: str = input("Enter a value (or just press enter to finish): ")
        if value == "":
            break
        values.append(value)

    print("Here's the list:", values)


print('\n===== 11. Get User List =====')
get_user_list()

