# Create  a  function  that  calculates  the  power  of  a  number.
# Then  write a unit test to check the correctness of the function


def exponent(num, expo):
    result = 1
    for i in range(expo):
        result *= num
    return result


print(pow(2, 5))
print(exponent(7, 5))
