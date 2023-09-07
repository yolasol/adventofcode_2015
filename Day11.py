import re

# rule 1: one increasing straight of at least 3 letters
# I can't figure out a non stupid way to do this
rule_one = re.compile(r"abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz")

# rule 2: may not contain i, o, or l
rule_two = re.compile(r"[iol]]")

# rule 3: must contain at least 2 different, non-overlapping pairs of letters
# any character (.), \1 matches the 1st capturing group, \2 matches the 2nd capturing group
# separated by any character repeated between zero and unlimited times .*
rule_three = re.compile(r"(.)\1.*(.)\2")

# functions are cool
# check if password is valid
def check_password(check: str) -> bool:
    if not rule_one.search(check):
        return False

    if rule_two.search(check):
        return False

    if not rule_three.search(check):
        return False
    elif rule_three.search(check):
        # check if both pairs are different:
        p1, p2 = rule_three.groups()
        if p1 == p2:
            return False

    return True


# recursive functions are cooler
# generate a new password
def create_password(password: str) -> str:
    i = len(password) - 1
    char = password[i]
    rest = password[:-1]
    newchar = next_char(char)

    if newchar == "a":
        rest = create_password(rest)

    new_pwd = rest + newchar

    return new_pwd


def next_char(some_char: str) -> str:
    if some_char != "z":
        # ord() turns character into integer (unicode), chr() turns integer back into character
        return chr(ord(some_char)+1)
    else:
        return "a"


# keep generating new passwords until one passes the check
def solve(new_pwd: str):
    valid = False
    while not valid:
        try:
            new_pwd = create_password(new_pwd)
            valid = check_password(new_pwd)
        except:
            print("het gaat niet goed")
            break

    return new_pwd


def main():
    password = "cqjxxyzz"
    new_password = solve(password)
    print(new_password)

main()

