from timer import timer
import random_list

comparisions = {
    "bubble":0,
    "selection":0,
    "insertion":0,
    "shell":0
}

@timer
def bubble_sort(arr):
    print("BUBBLE SORT: ")
    print(arr)
    n = len(arr)
    for i in range(0,n-1):
        sorted = 1
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                sorted = 0
            comparisions["bubble"]+=1
        print(arr)
        if sorted:
            break

@timer
def selection_sort(arr):
    print("SELECTION SORT: ")
    print(arr)
    n = len(arr)
    for i in range(0,n-1):
        x = i
        for j in range(i+1,n):
            if (arr[j]<arr[x]):
                x = j
            comparisions["selection"]+=1
        arr[x],arr[i] = arr[i],arr[x]
        print(arr)

@timer
def insertion_sort(arr):
    print("INSERTION SORT:")
    print(arr)
    n = len(arr)
    for i in range(1,n):
        j = i-1
        temp = arr[i]
        comparisions["insertion"]+=1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1
            comparisions["insertion"]+=1
        print(arr)
        arr[j+1] = temp
    

@timer
def shell_sort(arr):
    print("SHELL SORT: ")
    print(arr)
    n = len(arr)
    gap = n//2
    while gap>0:
        i=0
        while (i+gap<n):
            if (i>=0 and arr[i]>arr[i+gap]):
                arr[i],arr[i+gap] = arr[i+gap],arr[i]
                i-=gap
            else:
                i = max(0,i+1)
        gap//=2
        print(arr)


def compare(test_arr):
    n = len(test_arr)
    print("\n")
    print("*"*100,"\n")
    print("For size",n,"\n")
    print("EXECUTION TIME\n")

    arr = test_arr.copy()
    bubble_sort(arr)

    arr = test_arr.copy()
    selection_sort(arr)

    arr = test_arr.copy()
    insertion_sort(arr)

    arr = test_arr.copy()
    shell_sort(arr)

    print("\nNO OF COMPARISIONS: \n")
    for key,value in comparisions.items():
        print(f"{key} sort: {value}")
        comparisions[key] = 0

# compare(random_list.list10)
# compare(random_list.list100)
# compare(random_list.list1000)
# compare(random_list.list10000)

arr = random_list.generate_random(10)

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
    arr = random_list.generate_random(10)