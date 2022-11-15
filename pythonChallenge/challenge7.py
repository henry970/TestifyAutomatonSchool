#  Create a program that prints out the odd numbers in an array.
#  Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,401, 0]

def print_odd_numbers(arr):
    odd_numbers = []
    for i in arr:
        if i % 2 != 0:
            odd_numbers.append(i)
    print(odd_numbers)


print_odd_numbers([1, 2, 3, 4, 5, 6])
print_odd_numbers([34, 2, 9, 91, 19, 401, 0])