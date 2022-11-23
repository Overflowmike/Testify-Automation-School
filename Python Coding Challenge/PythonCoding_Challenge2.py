
# Write a function that calculate the power of a number. Then write a unit test to check the correctness of the function


def power(n, e):
    res = 0
    for i in range(e):
        res *= n
    return res


print(pow(5, 2))

