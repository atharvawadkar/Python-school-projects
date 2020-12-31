#write a program to store first year percentage of student in by array
#write function for string array of floating  point number is acsending order using
#a)Slection sort and display top five scores
#b)bubble sort and display top five scores


a,b=10,20
print(a,b)
a,b=b,a
print(a,b)

def in_put():
    arr1=[]
    Num=int(input("Enter the number of students "))
    for i in range(Num):
        per=float(input("Enter the percentage marks "))
        arr1.append(per)
    prit(arr1)
    return arr1


def prit_top(arr1):
    print("top five scores  are")
    j=(len(arr1)-1)
    for i in range(1,6):
        print(i,".""%.lf"%arr1[j])
        j=j-1

def prit(arr1):
    for i in range (len(arr1)):
        print("%f"%arr1[i])

def BubbleSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def SelectionSort(arr):

    for i in range(len(arr)):
        min_idx =i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j

        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr





# def in_put():
#     arr1=[]
#     Num=int(input("Enter the number of students "))
#     for i in range(Num):
#         per=float(input("Enter the percentage marks "))
#         arr1.append(per)
#     prit(arr1)






def main():
    arr=[]
    arr=in_put()
    cho=0
    while(cho!=3):
        print("1.Bubble sort \n 2 . selection sort \n 3. Exit \n\n Enter your choice ")
        cho=int(input())
        if cho==1:
            arr=BubbleSort(arr)
            prit(arr)
            prit_top(arr)
        elif cho==2:
            arr =SelectionSort(arr)
            prit(arr)
            prit_top(arr)
        elif cho==3:
            quit()

main()

