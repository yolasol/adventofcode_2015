# part 1
# get input
input = open("day2_input.txt")

# calculate the surface area for each box, add to total
paper = 0

for box in input:
     l, w, h = box.split('x')
     l, w, h = int(l), int(w), int(h)

     slack = min(l*w, w*h, h*l)
     paper += (2*l*w) + (2*w*h) + (2*h*l) + slack

# total square feet of wrapping paper needed
print(paper)


# part 2
# get input
input = open("day2_input.txt")

# calculate the surface area for each box + slack, add to total paper
# calculate smallest perimeter + bow, add to total ribbon
paper = 0
ribbon = 0

for box in input:
    l, w, h = box.split('x')
    l, w, h = int(l), int(w), int(h)

    slack = min(l*w, w*h, h*l)
    paper += (2*l*w) + (2*w*h) + (2*h*l) + slack

    bow = l * w * h
    ribbon += 2 * min(l+w, w+h, h+l) + bow

# total square feet of wrapping paper and total feet of ribbon needed
print(paper, ribbon)