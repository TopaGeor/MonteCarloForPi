import random
from math import pi


def main():
    # initialization
    decimals = 5
    tries = 100
    points = 10 ** decimals
    results = []
    smallest_difference = 2

    approximate_pi = pi * points
    approximate_pi = int(approximate_pi)
    approximate_pi /= points

    while (tries):
        count = 0
        for i in range(0, points):
            x = random.random()
            y = random.random()
            if (((x * x + y * y) ** 0.5) < 1):
                count += 1

        result = (count * 4) / points
        if (abs(result - approximate_pi) < abs(smallest_difference)):
            smallest_difference = result - approximate_pi
            best_solution = result

        tries -= 1
        results.append(result)

    print("The smallest calculated π is: ", best_solution)
    print("While all of the results are:", results)


if __name__ == "__main__":
    main()
