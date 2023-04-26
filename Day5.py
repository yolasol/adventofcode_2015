# part 1
import re
# get input
with open("day5_input.txt") as input:
    list = input.readlines()

# check each string for niceness
vowels = re.compile(r"([aeiou].*){3,}")
double = re.compile(r"(.)\1")
naughty = re.compile(r"ab|cd|pq|xy")

# how many strings are nice?
nice = 0

for word in list:
    if vowels.search(word) and double.search(word) and not naughty.search(word):
        nice += 1

print(nice)

# part 2
# new rules
xx = re.compile(r"(..).*\1")
xyx = re.compile(r"(.).\1")

# how many strings are nice?
nice = 0

for word in list:
    if xx.search(word) and xyx.search(word):
        nice += 1

print(nice)






