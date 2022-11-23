
# Create a function that converts any string  value to a sentence case, then
# write a unit test that check the function's correctness

def proper(senTense):
    words = senTense.split(". ")
    new = ". ".join([word.capitalize() for word in words])
    return new


senTense = "this is string. and this is another string."
n = proper(senTense)
print(proper(senTense))
# output:- This is string. And this is another string.