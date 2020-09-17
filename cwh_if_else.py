try:
 age = int(input("Enter your age:"))
except:
    print("Invalid value")
    quit()
if 100 > age > 18:
    print("Good to go")
elif age == 18 :
    print("To be determined ")
else :
    print("improper age")

