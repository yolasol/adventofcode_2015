import re

# functions are cool
def solve(thing: str, n: int):

    for i in range(n):
        new_num = ""

        while True:
            # any digit (\d) at the start of the string (^) repeated between zero and unlimited times (\1*)
            digits = re.match(r"^(\d)\1*", thing)
            # turn digits into something that can be returned
            if digits:
                digits = digits.group(0)
            if len(thing) == 0:
                thing = new_num
                break

            # replace group by length of the group plus the original digit
            j = len(digits)
            thing = thing[j:]
            new_num += str(len(digits))
            new_num += digits[0]

    return len(new_num)

# part 1
print(solve("3113322113", 40))

# part 2
# part 1 was already a bit clunky but doing it 50 times will take forever. Different approach!
def solve_but_better(thing: str, n: int):
    result = ""

    for i in range(n):
        counts = []
        count = 0
        previous = None

        for digit in thing:
            if (previous and digit != previous):
                counts.append([count, previous])
                count = 0

            count += 1
            previous = digit

        counts.append([count, previous])

        thing = "".join(str(num) + str(digit) for num, digit in counts)

    return len(thing)

print(solve_but_better("3113322113", 50))



