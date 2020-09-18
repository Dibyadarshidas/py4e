a = dict()
n =int(input("number of elements:"))

for i in range(n):
    k = input("Enter Key:")
    v = input("Enter Value:")
    a.update({k:v})
print(a)