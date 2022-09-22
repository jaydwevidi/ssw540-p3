"""

Author : Pranjal Apoorva
P3: User defined functions
Python script that takes three values and returns the maximum value of the three

"""


def maxOfThree(x, y, z):
    try:
        x1 = float(x)
        y1 = float(y)
        z1 = float(z)
        c = 1
        if y > x and y > z:
            return y
        elif z > x and z > y:
            return z
        else:
            return x
    except:
        return "\nInvalid input. Please try again."


def main():
    a = input("Enter first value: ")
    b = input("Enter second value: ")
    c = input("Enter third value: ")
    v = maxOfThree(a, b, c)
    if v != "\nInvalid input. Please try again.":
        print("\nThe maximum of", a, b, c, "is", v)
    else:
        print(v)


main()
