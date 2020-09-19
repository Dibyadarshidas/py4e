n = 18
counter = 9
while counter >= 0:

    print("Guess the number: ")
    user = int(input())

    if user == n:
        print("You Won!")
        print("You have guessed the number in " + "First" + " attempt")

        break

    else:
        print("Wrong number!")
        print("You have " + str(counter) + " attempts left")
        counter = counter - 1
        continue
