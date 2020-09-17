count = 0
while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print("invalid input")
        continue
    if count == 0:
        min_val = fnum
        max_val = fnum
    elif fnum > max_val:
        max_val = fnum
    elif fnum < min_val:
        min_val = fnum
    count += 1
print("All DONE")
print("minimum value:",min_val,"maximum value:",max_val)



