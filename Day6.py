import re

# get input
with open("day6_input.txt") as input:
    instr = input.readlines()

# part 1
# create a grid of lights
# all lights are off at the start
thing = []
for x in range (1000):
    for y in range(1000):
        thing.append((y,x))

# lights please
known = [False for i in range(1000000)]
lights = dict(zip(thing, known))

# how to use the input
def turnOn(a, b, c, d):
    for z in range(a, c + 1):
        for zz in range(b, d + 1):
            lights[z, zz] = True

def turnOff(a, b, c, d):
    for z in range(a, c + 1):
        for zz in range(b, d + 1):
            lights[z, zz] = False

def toggle(a, b, c, d):
    for z in range(a, c + 1):
        for zz in range(b, d + 1):
            lights[z, zz] = not lights[z, zz]

# do the thing
nums = re.compile(r"(\d+),(\d+) through (\d+),(\d+)")

# groups() returns a tuple with all subgroups (the things in parentheses)
# map() iterates over the subgroups found by groups()
for line in instr:
    coordinates = nums.search(line)
    assert coordinates, "nope"
    a, b, c, d = map(int, coordinates.groups())
    if "on" in line:
        turnOn(a,b,c,d)
    elif "off" in line:
        turnOff(a,b,c,d)
    elif "toggle" in line:
        toggle(a,b,c,d)

# how many lights are on
# values() returns a view object, which contains the values of the dictionary as a list
# count(x) returns the number of elements with the value x
print(f"{list(lights.values()).count(True)} lights are now on")

# part 2
# lights have a brightness instead of boolean state
# all lights start at a brightness of zero
thing = []
for x in range (1000):
    for y in range(1000):
        thing.append((y,x))

# lights please
known = [0 for i in range(1000000)]
lights = dict(zip(thing, known))

# how to use the input
def increase(a, b, c, d):
    for z in range(a, c + 1):
        for zz in range(b, d + 1):
            lights[z, zz] += 1

def decrease(a, b, c, d):
    for z in range(a, c + 1):
        for zz in range(b, d + 1):
            if lights[z,zz] > 0:
                lights[z, zz] -= 1

def toggle2(a, b, c, d):
    for z in range(a, c + 1):
        for zz in range(b, d + 1):
            lights[z, zz] += 2

# groups() returns a tuple with all subgroups (the things in parentheses)
# map() iterates over the subgroups found by groups()
for line in instr:
    coordinates = nums.search(line)
    assert coordinates, "nope"
    a, b, c, d = map(int, coordinates.groups())
    if "on" in line:
        increase(a,b,c,d)
    elif "off" in line:
        decrease(a,b,c,d)
    elif "toggle" in line:
        toggle2(a,b,c,d)

# total brightness of all the lights
brightness = 0

for light in lights:
    brightness = brightness + lights[light]

print(f"The total brightness is {brightness}")
