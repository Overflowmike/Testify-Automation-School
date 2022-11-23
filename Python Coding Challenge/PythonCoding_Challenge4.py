
# Write a well documented code to create a function that calculate simple interest


def simpleInterset(P, T, R):

    # P = 'principal'
    # T = 'time in days'
    # R = 'rate'

    SI = (P * T * R) / 100
    return SI


print(simpleInterset(50000, 30, 5))