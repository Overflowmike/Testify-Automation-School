
# Write a python program to check if a string is a palindrome.Then optionally write a unit test
# your program correctness

x = "malayalam"

w = ""
for i in x:
    w = i + w

if x == w:
    print("Yes")
else:
    print("No")