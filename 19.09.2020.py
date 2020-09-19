# Sort by values instead of key
#c = {'a':10, 'b':1, 'c':22 }
#tmp = []
#for k, v in c.items() :
#    tmp.append((v, k))
#print(tmp)
#tmp = sorted(tmp, reverse=True)
#print(tmp)
# Long Method
#fhand =open('words.txt')
#counts = {}
#for line in fhand:
#    words = line.split()
#    for word in words:
#        counts[word] = counts.get(word, 0) + 1

#lst = []
#for k,v in counts.items():
#    newtup = (v, k)
#    lst.append(newtup)
#lst = sorted(lst,reverse=True)
#for v,k in lst[:10]:
#    print(k,v)
# Shorter Version
#c = {'a': 10 , 'b' : 1 , 'c': 22}
#print(sorted([(v,k) for k,v in c.items()],reverse=True))
