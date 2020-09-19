print ("Welcome to guess the number game!")
print ("Follow given hint to find the number")
print ("The number is a two digit number")
n = 63
c = 6
while c >= 1:
    guess = int(input("Guess the number "))
    if guess == n:
        print ("Yo man you won!!")
        break
    elif guess > 63:
        print ("Decrease the number ")
        c = c-1
        print ("Chances left =", c)
        continue
    elif guess < 63:
        print ("Increase your number ")
        c = c -1
        print ("Chances left =", c)
        continue
print("GAME OVER\n""TRY AGAIN")

