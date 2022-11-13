while True:  # a while loop it go when the loop is true

    try:

        height = int(input("Height: "))  # geting hight

        if (height >= 1) and (height <= 8):  # checking the input

            break  # if true break

    except:  # except ""

        print("", end="")

for row in range(height):  # printing the row

    for space in range(height - row - 1, 0, -1):  # printg the space without /n

        print(" ", end="")

    for hash in range(row + 1):  # printing the hash without /n

        print("#", end="")

    print()  # if you are crazy you can use => print("\n", end ="")
# if you are thinking I'm doing this because I'm scered of style50 you are right !!