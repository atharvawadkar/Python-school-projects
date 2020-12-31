a=list(map(int,input().rstrip().split()))
b=list(map(int,input().rstrip().split()))

e = [0, 0



for i in range(3):

    if a[i] > b[i]:
        e[0] = e[0] + 1
    elif a[i]==b[i] :
        e[0]=e[0]
        e[1]=e[1]
    else:
        e[1] = e[1] + 1


print(e[0], e[1])


