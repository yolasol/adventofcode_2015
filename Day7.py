import re

# get input
with open("day7_input.txt") as f:
    instr = f.readlines()

# make a dictionary to keep wires and values
wires = {}

# do something with the instructions
# write a function because that's cool
def solve(line):
    # define the options
    # after the arrow
    target = re.compile(r"-> (\w+)")
    target_wire = target.search(line).group(1)

    # before the arrow
    no = re.compile(r"NOT (\w+) ->")
    other = re.compile(r"(\w+) (AND|OR|LSHIFT|RSHIFT) (\S+) ->")
    connect = re.compile(r"(\S+) ->")

    # solve NOT
    if no.search(line):
        wire_value = wires[no.search(line).group(1)]
        # convert to 16-bit(!) binary signal
        wire_binary = bin(wire_value)[2:].zfill(16)
        val = ''

        for bit in wire_binary:
            if bit == "1":
                val += "0"
            else:
                val += "1"
        value = int(val, 2)

    # solve AND|OR|LSHIFT|RSHIFT
    elif other.search(line):
        thing1 = other.search(line).group(1)
        operation = other.search(line).group(2)
        thing2 = other.search(line).group(3)

        if thing1.isnumeric():
            one = int(thing1)
        else:
            one = wires[thing1]

        if thing2.isnumeric():
            two = int(thing2)
        else:
            two = wires[thing2]

        # Python already converts to binary for bitwise operators, yay
        if operation == "AND":
            value = one & two
        elif operation == "OR":
            value = one | two
        elif operation == "LSHIFT":
            value = one << two
        elif operation == "RSHIFT":
            value = one >> two

    # solve connect
    elif connect.search(line):
        new_value = connect.search(line).group(1)
        if new_value.isnumeric():
            value = new_value
        else:
            value = wires[new_value]

    # can we add a value to a wire
    try:
        wires[target_wire] = int(value)
    except:
        return

    return True

# do the thing
# if the instruction cannot be solved, keep going
while instr:
    done = []
    for line in instr:
        try:
            if solve(line):
                done.append(line)
        except:
            continue
    # remove line if solved
    for d in done:
        instr.remove(d)

# part 1
print("the answer to part 1:", wires['a'])

# part 2
# save value on wire a
val = wires['a']

# reset all values, set wire b to the value saved from wire a
wires = {}
wires['b'] = val

# get the instructions again
with open("day7_input.txt") as f:
    instr = f.readlines()

# ignore any initial setting of wire b
ignore = re.compile(r"(\d+) -> b$")

for line in instr:
    if ignore.search(line):
        instr.remove(line)

# rerun the whole thing
while instr:
    done = []
    for line in instr:
        try:
            if solve(line):
                done.append(line)
        except:
            continue
    # remove line if solved
    for d in done:
        instr.remove(d)

print("the answer to part 2:", wires['a'])