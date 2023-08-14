from ast import literal_eval
import re

# get the input
# readlines() adds newlines, splitlines() doesn't
with open("day8_input.txt") as f:
    instr = f.read().splitlines()

# functions are cool
def solve(thing):
    # count everything
    everything = []

    for line in thing:
        everything.append(len(line))

    # count values
    values = []

    for line in thing:
        literal = literal_eval(line)
        values.append(len(literal))

    print(f"part 1: {sum(everything) - sum(values)}")

# part 1
solve(instr)

# part 2
def reverse(thing):
    # count everything
    reverse = []

    for line in thing:
        reverse.append(len(line))

    # quotation marks, put \ in front of any " and \, count values
    reverse_values = []

    for line in thing:
        # match any character in the list of " and \
        # replace 1st group (\1) with \ + 1st group
        tmp = r'"' + re.sub(r'(["\\])', r"\\\1", line) + r'"'
        reverse_values.append(len(tmp))

    print(f"part 2: {sum(reverse_values) - sum(reverse)}")

reverse(instr)
