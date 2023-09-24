l = input()
p=""
i=0
while i< len(l):
    if l[i] == "p":
        i+=1
    p+=l[i]
    i+=1
print(p)