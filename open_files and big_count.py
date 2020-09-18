name = input("Enter file:")
handle = open(name)
counts = dict()
bigcount = None
bigword = None
smallcount = None
smallword = None
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
#print(counts)
for p,q in counts.items():
    print(p,q)
    if bigcount is None or q > bigcount:
        bigword = p
        bigcount = q
print("Highest Occurrence:",bigword,bigcount)

