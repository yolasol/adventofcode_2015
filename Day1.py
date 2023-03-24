# part 1
# set starting floor
floor = 0

# get instructions
txt = open("day1_instructions.txt")
instructions = txt.read()

# read instructions, adjust floor
for char in instructions:
    if char == "(":
        floor += 1
    else:
        floor -= 1

# present outcome
print(floor)

# part 2
# set floor to zero again, add basement
floor = 0
basement = 0

# read instructions, adjust floor and basement
for char in instructions:
    basement +=1
    if char == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(basement)
        break
