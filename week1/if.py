# if, elif, else with boolean expressions

# Example 1: Basic if-else statement
# a = 20
# a = 5
# b = 10
# if a < b:
#     print("a is less than b")
#
# elif a > b:
#     print("a is greater than b")

# Example 2: logic if-else statement

a = 5
b = 10
c = 30

if (a> b) and (a > c):
    print("a số lon nhất")

if (a < b) or (a < c):
    print("a số bé nhất")

if (a == b) and (a == c):
    print("a bằng b và c")

if (a != b) and (a != c):
    print("a khác b và c")

if (a >= b) and (a >= c):
    print("a lớn hơn hoặc bằng b và c")

d = True
if not d:
    print("d là False")
else:
    print("d là True")
