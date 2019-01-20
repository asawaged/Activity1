def main():
    grade = float(input("Enter total number of points earn: "))
    if grade > 919.9 and grade <= 1000:
        print("Letter Grade: A")
    elif grade > 879 and grade <= 919.9:
        print("Letter Grade: B+")
    elif grade > 819.9 <= 879.9:
        print("Letter Grade: B")
    elif grade > 779 and grade <= 819.9:
        print("Letter Grade: C+")
    elif grade > 699.9 and grade <= 779.9:
        print("Letter  Grade: C")
    elif grade >= 600 and grade <= 699.9:
        print("Letter Grade: D")
    elif grade < 600:
        print("Letter Grade: F")

    choice = input('Continue? y/n ')

    if choice == 'n':
        exit()
    else:
        main()


main()
