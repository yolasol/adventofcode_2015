# make a class Santa because why not
# Santa needs a location, a history of locations, and directions to follow
class Santa:
    def __init__(self, location, visited):
        self.location = location
        self.visited = visited

    # Santa also needs a way to move
    def move(self, directions):
        for char in directions:
            if char == "^":
                self.location = [self.location[0], self.location[1] + 1]
            elif char == ">":
                self.location = [self.location[0] + 1, self.location[1]]
            elif char == "v":
                self.location = [self.location[0], self.location[1] - 1]
            elif char == "<":
                self.location = [self.location[0] - 1, self.location[1]]

            if self.location not in self.visited:
                self.visited.append(self.location)

    def delivered(self):
        print(f"This Santa has delivered presents to {len(self.visited)} houses")

# get directions
with open("day3_input.txt") as f:
    directions = f.read()

# part 1: original Santa
OriginalSanta = Santa([0,0], [[0,0]])

# part 2: Real-Santa and Robo-Santa
RealSanta = Santa([0,0], [[0,0]])
RoboSanta = Santa([0,0], [[0,0]])

# make all santas move
OriginalSanta.move(directions)
RealSanta.move(directions[0::2])
RoboSanta.move(directions[1::2])

# part 1: how many houses did Santa visit at least once
OriginalSanta.delivered()

# part 2: how many houses were visited at least once by Real-Santa or Robo-Santa
print(RealSanta.visited)
print(RoboSanta.visited)

Houses = RealSanta.visited

for house in RoboSanta.visited:
    if house not in Houses:
        Houses.append(house)

print(len(Houses))