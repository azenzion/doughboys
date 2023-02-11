import random

flavours = range(1, 19)

def pickFlavours():
    # There are two people
    # Each picks 3 flavours at random
    # no repeats

    # Person 1
    p1 = random.sample(flavours, 3)

    # Person 2
    p2 = random.sample(flavours, 3)

    # turn the lists into sets
    # This is so the order of the flavours doesn't matter
    p1 = set(p1)
    p2 = set(p2)

    # Return 1 if they pick the same 3 flavours
    # Return 0 if they don't
    if p1 == p2:
        return 1
    else:
        return 0

def main():
    # Count the number of times they pick the same 3 flavours
    # Print the result

    trials = 10000000

    count = 0
    for i in range(trials):
        count += pickFlavours()

    print("They pick the same 3 flavours", count, "times")

    print("The probability of them picking the same 3 flavours is", count/trials)

    print("That is one in every", trials/count, "trials")


if __name__ == "__main__":
    main()
