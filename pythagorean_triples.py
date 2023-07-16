#Brayden Jonsson, July 2023

import argparse # for command line arguments
import math # for square roots

def pythagorean_triples(hypotenuse, sideLength, maximumValue=0):
    """This finds all pythagorean triples that contain the given side and fit within the given maximum value (if applicable)

    hypotenuse is a bool defining if the given side is the hypotenuse or not.

    sideLength is a positive integer defining the side length of the given side.

    maximumValue defines the maximum tested value, only if hypotenuse is false. This is not required if hypotenuse is true.

    Returns a list of lists, where the outer list contains all found pythagorean triples and each inner list contains an individual triple where the first two items are the two legs, and the last item is the hypotenuse, sorted by length."""

    if not type(hypotenuse) is bool:
        raise TypeError("hypotenuse must be a boolean!")
    if not type(sideLength) is int:
        raise TypeError("sideLength must be an integer!")
    if not type(maximumValue) is int:
        raise TypeError("maximumValue must be an integer!")

    successfulTriples = []
    if hypotenuse:
        for legA in range(1, sideLength):
            for legB in range(legA):
                testHypotenuse = math.sqrt((legA**2) + (legB**2))
                if testHypotenuse == sideLength:
                    successfulTriples.append([legB, legA, sideLength])
                elif testHypotenuse > sideLength:
                    break
    else:
        if maximumValue <= 0:
            raise ValueError("maximumValue is required if hypotenuse is false!")
        sideLengthSquared = sideLength**2
        for legA in range(1, maximumValue):
            testHypotenuse = math.sqrt(sideLengthSquared + legA**2)
            if testHypotenuse.is_integer():
                testHypotenuse = int(testHypotenuse)
                if sideLength > legA:
                    successfulTriples.append([legA, sideLength, testHypotenuse])
                else:
                    successfulTriples.append([sideLength, legA, testHypotenuse])

    return successfulTriples



if __name__ == "__main__":
    description = "This script takes in the given arguments, to determine all valid pythagorean triples with these values"

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-l", "--Hypotenuse", help="Set to true if the given Side_Length represents the hypotenuse", type=bool, default=False)
    parser.add_argument("-s", "--Side_Length", help="The side length of the known side.", type=int, required=True)
    parser.add_argument("-m", "--Maximum_Value", help="If hypotenuse is false, then this determines the maximum tested value of the second side", type=int, default=0)

    args = parser.parse_args()

    triples = pythagorean_triples(args.Hypotenuse, args.Side_Length, args.Maximum_Value)

    if len(triples) == 1:
        print("Found 1 Pythagorean Triple.")
    else:
        print(f"Found {len(triples)} Pythagorean Triples.")
    for triple in triples:
        print(*triple, sep = ", ")
    print("All triples printed.")
