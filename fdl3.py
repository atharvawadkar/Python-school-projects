# addition of the two matrix
row = int(input("Enter the num of row"))
coloumn = int(input("Enter the num of coloumn "))
matrixa = []
matrixb = []
resultadd = []
resultsub = []
resultmul = []
trans=[]
print("Enter the number rowise")
# for input
for i in range(row):
    a = []
    for j in range(coloumn):
        a.append(int(input()))
    matrixa.append(a)


# for printing matrix
def prt():

    for i in range(0, row):
        for j in range(0, coloumn):
            print(matrixa[i][j],end="")
        print()
prt()
# for input
for i in range(0, row):
    b = []
    for j in range(0, coloumn):
        b.append(int(input()))
    matrixb.append(b)

# for printing matrix
for i in range(0, row):
    for j in range(0, coloumn):
        print(matrixb[i][j], end=" ")

# for addition
for i in range(0, row):
    c = []
    for j in range(0, coloumn):
        c.append(matrixa[i][j] + matrixb[i][j])
    resultadd.append(c)

# for result
for i in range(0, row):
    for j in range(0, coloumn):
        print(resultadd[i][j], end=" ")
    print()

# for sub
for i in range(0, row):
    c = []
    for j in range(0, coloumn):
        c.append(matrixa[i][j] - matrixb[i][j])
    resultsub.append(c)

# for result
for i in range(0, row):
    for j in range(0, coloumn):
        print(resultsub[i][j], end=" ")
    print()

c = 0
for i in range(row):
    a = []
    # iterating by coloum by B
    for j in range(coloumn):

        # iterating by rows of B
        for k in range(row):
            c = c + matrixa[i][k] * matrixb[k][j]
        a.append(c)
        c = 0
        resultmul.append(a)

        # for resultmul
for i in range(0, row):
    for j in range(0, coloumn):
                print(resultmul[i][j], end=" ")
    print()

#transpose
for i in range(row):
    a=[0]
    for j in range(coloumn):
        a.append(0)
    trans.append(a)
for i in range(row):
    for j in range(coloumn):
        trans[j][i]=matrixa[i][j]

for i in range(0, row):
    for j in range(0, coloumn):
                print(trans[i][j], end=" ")
    print()