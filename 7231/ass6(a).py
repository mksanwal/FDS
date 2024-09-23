
def bubble_sort(arr):
    print("BUBBLE SORT: ")
    n = len(arr)
    comparison = 0
    for i in range(0,n-1):
        sorted = 1
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                sorted = 0
            comparison+=1
        print(arr)
        if sorted:
            break
    print("Number of comparisons are: ",comparison)
        

def selection_sort(arr):
    print("SELECTION SORT: ")
    print(arr)
    n = len(arr)
    comparison = 0
    for i in range(0,n-1):
        x = i
        for j in range(i+1,n):
            if (arr[j]<arr[x]):
                x = j
            comparison+=1
        arr[x],arr[i] = arr[i],arr[x]
        print(arr)
    print("Number of comparisons are: ",comparison)


def insertion_sort(arr):
    print("INSERTION SORT:")
    print(arr)
    n = len(arr)
    comparison = 0
    for i in range(1,n):
        j = i-1
        temp = arr[i]
        comparison+=1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1    
        print(arr)
        arr[j+1] = temp
    print("Number of comparisons are: ",comparison)    
    


def shell_sort(arr):
    print("SHELL SORT: ")
    print(arr)
    n = len(arr)
    comparison = 0
    gap = n//2
    while gap>0:
        i=0
        
        while (i+gap<n):
            comparison+=1
            if (i>=0 and arr[i]>arr[i+gap]):
                arr[i],arr[i+gap] = arr[i+gap],arr[i]
                i-=gap
            else:
                i = max(0,i+1)
        gap//=2
        print(arr)
    print("Number of comparisons are: ",comparison)


arr = [345, 782, 156, 923, 468, 739, 215, 657, 284, 391, 508, 631, 950, 742, 107, 892, 344, 219, 526, 731, 694, 808, 172, 456, 239, 307, 561, 417, 643, 885, 198, 762, 914, 327, 480, 294, 548, 769, 350, 825, 612, 473, 197, 608, 795, 221, 319, 680, 932, 405, 592, 289, 743, 870, 146, 702, 518, 904, 337, 788, 134, 274, 758, 329, 590, 416, 201, 915, 745, 352, 483, 295, 674, 102, 310, 568, 823, 482, 430, 964, 175, 611, 420, 299, 683, 137, 247, 831, 471, 209, 334, 802, 359, 890, 427, 73, 65, 300, 200, 501]

menu = """*********************************************
0. Exit
1. Bubble Sort
2. Insertion Sort
3. Selection Sort
4. Shell Sort
*********************************************"""

ch = -1
while ch!=0:
    print(menu)
    ch = int(input("Enter your choice: "))
    print("Original array:",arr)
    if ch==0:
        print("Exiting the program...")
        exit(0)
    elif ch==1:
        bubble_sort(arr)
    elif ch==2:
        insertion_sort(arr)
    elif ch==3:
        selection_sort(arr)
    elif ch==4:
        shell_sort(arr)
    else:
        print("Invalid Choice")
    print("Sorted array:",arr)
