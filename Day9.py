import re
from itertools import permutations

# get the data
with open("day9_input.txt") as f:
    instr = f.readlines()

# functions are cool
# create a dictionary containing every possible pair of locations and the distance between them
def find_distances(thing):
    distances = {}
    stuff = re.compile(r"(\w+) to (\w+) = (\d+)")

    for line in thing:
        city1, city2, distance = stuff.findall(line)[0]
        distance = int(distance)

        distances[(city1, city2)] = distance
        distances[(city2, city1)] = distance

    return distances

def solve(thing):
    # make a list of all locations
    locations = set()
    distances = find_distances(thing)
    possibilities = []
    route = []

    for cities in distances:
        locations.add(cities[0])
        locations.add(cities[1])

    # for every possible combination of locations
    for permutation in permutations(locations):
        # add all distances between the locations in this permutation
        total_distance = 0

        for i in range(len(permutation)-1):
            city1 = permutation[i]
            city2 = permutation[i+1]
            distance = distances[(city1, city2)]
            total_distance += distance

        # store the total distance
        # this is somewhat redundant since ABC = CBA but hey
        # I don't have to know which route it is but I'm including it for fun
        possibilities.append(total_distance)
        if total_distance == min(possibilities):
            route = permutation
        if total_distance == max(possibilities):
            route2 = permutation

    # get the answer to part 1 and part 2
    return(f"The shortest possible distance is {min(possibilities)} \n"
           f"This is the shortest route: {route} \n"
           f"The longest possible distance is {max(possibilities)} \n"
           f"This is the longest possible route: {route2}")

print(solve(instr))

