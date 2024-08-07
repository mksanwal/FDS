n = int(input("Enter the number of students: "))
sum = 0
list_of_marks = [] 
absent = 0
t = n
p = 0
f = 0

while n > 0:
    mks = int(input("Enter the marks of the student: "))
    sum += mks  

    if mks < 0:
        absent += 1
    else:
        list_of_marks.append(mks)

    if mks >= 40:
        p += 1
    else:
        f += 1

    n -= 1 

avg_marks = sum / len(list_of_marks) if list_of_marks else 0
print("Average marks:", avg_marks)

list_of_marks.sort()
print("Lowest marks:", list_of_marks[0] if list_of_marks else "No marks available")
print("Highest marks:", list_of_marks[-1] if list_of_marks else "No marks available")

percentage_passed = (p / t )* 100 
percentage_failed = ((f-absent) / t) * 100 
print("Percentage of passed students:", percentage_passed)
print("Percentage of failed students:", percentage_failed)


freq = 0
ele = 0
for i in range(0,t):
    count = 0
    for j in range(0,t):
        if(list_of_marks[i] == list_of_marks[j]):
            count+=1
    if(freq < count):
        freq = count
        ele = list_of_marks[i]

print("Marks with highest frequency: ",ele)