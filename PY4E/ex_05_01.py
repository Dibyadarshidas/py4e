num = 0
tot = 0.0
while True:
    sval = input("Enter a number:")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("invalid input")
        continue
    num += 1
    tot = tot + fval
print("All DONE")
print(tot,num,tot/num)