#Antonio Bernal
#ITSE 1302-004
#09/15/2021


def main():
    print("Enter the Length and Width for the FIRST rectangle: ")
    length1 = float(input("Length: "))
    width1 = float(input("Width: "))

    print("Enter the Length and Width for the SECOND rectangle: ")
    length2 = float(input("Length: "))
    width2 = float(input("Width: "))

    rectangle1 = length1 * width1
    rectangle2 = length2 * width2

    if rectangle1 > rectangle2:
        print("The first rectangle has the greater area")
    if rectangle1 < rectangle2:
        print("The second rectangle has the greater area")
    if rectangle1 == rectangle2:
        print("These two rectangles are equal!")

main()
