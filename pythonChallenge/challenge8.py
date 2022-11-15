# 8. Create a program that prints out the even numbers in an array.
# Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,40]


def print_even_numbers(arr):
    even_numbers = []
    for i in arr:
        if i % 2 == 0:
            even_numbers.append(i)
    print(even_numbers)


print_even_numbers([1, 2, 3, 4, 5, 6])
print_even_numbers([34, 2, 9, 91, 19, 401, 0])