
# Write a function that removes repeated characters from a string.
# Sample strings are: a Hello: output should be Helo
# b.Concatenate: output should be Conaten

# def dupe(str1):
#     s = set(str1)
#
#     return "".join(s)
#
#
# str1 = 'committee'
# a = dupe(str1)
# print(a)

def fix(string):
    s = set()
    list = []
    for ch in string:
        if ch not in s:
            s.add(ch)
            list.append(ch)

    return ''.join(list)


string = "Hello"
print(fix(string))

string = "Concatenate"
print(fix(string))