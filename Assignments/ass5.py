def linear_search(arr, chk):
    for index in range(len(arr)):
        if arr[index] == chk:
            return index
    return -1


def binary_search(arr, chk):
    p = 0
    
    arr.sort()
    f = 0
    l = len(arr) - 1
    while f <= l:
        p += 1
        mid = (f + l) // 2
        
        if arr[mid] == chk:
            return mid,p
        elif arr[mid] < chk:
            f = mid + 1
        else:
            l = mid - 1
    return -1,p



def sentinel_search(arr, chk): 
    n = len(arr)
    arr.append(chk)
    
    i = 0
    while arr[i] != chk:
        i += 1
    
    arr.pop()
    
    if i < n:
        return i
    else:
        return -1    


arr = list(map(int, input("Enter the roll numbers who attended the trainig program: ").split()))
chk = int(input("Enter the roll number to search for: "))
    




print("Linear search")
pos = linear_search(arr, chk)

if pos != -1:
    print("This student attended the training program and index is: ",pos)
    print("Number of time comparison performed during linear search is: ",pos+1) 
else:
    print("This student not attended the training program")
    print("Number of time comparison performed during linear search is: ",len(arr)) 
   






print("Binary search")
result,p = binary_search(arr,chk)

if result != -1:
    print("This student attended the training program")
else:
    print("This student not attended the training program")

print("Number of time comparison performed during binary search is: ",p)







print("Sentinel search")
index = sentinel_search(arr, chk)

if index != -1:
    print("This student attended the training program at index: ",index)
else:
    print("This student not attended the training program")