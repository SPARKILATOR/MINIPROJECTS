def remove_dup(n,n1):
    res1 = []
    res = []
    for i in range(0,len(n)):
        n[i] = list(str(n[i]))
        for j in n[i]:
            if n[i].count(j) != 1:
                n1.append("".join(n[i]))
                break
    for i in range(0,len(n)):
        res1.append("".join(n[i]))
    for i in range(0,len(res1)):
        if res1[i] not in n1:
            res.append(int(res1[i]))
    return res
#n = [4252, 6578, 3421, 6545, 6676]
length = int(input("Enter length of the list : "))
n = []
for i in range(length):
    n.append(int(input("Enter element : ")))
print("User input : ", n)
n1 = []
r = remove_dup(n,n1)
print("Expected Output : ", r)
