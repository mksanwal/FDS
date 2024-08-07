x = int(input("total number of students"))

a = int(input("number of student who play cricket"))
crk = []
while(a>0):
    num = int(input("Roll no. of students who play cricket"))
    crk.append(num)
    a-=1 


b = int(input("number of student who play badminton"))
bad = []
while(b>0):
    num = int(input("Roll no. of students who play badminton"))
    bad.append(num)
    b-=1


c = int(input("number of student who play football")) 
fb = []
while(c>0):
    num = int(input("Roll no. of students who play football"))
    fb.append(num)
    c-=1



# list of students who play both cricket and badminton
crk_and_bad = []
for student in crk:
    if student in bad and student not in crk_and_bad:
        crk_and_bad.append(student)

for p in crk_and_bad:
    print("Students who play both cricket and badminton :",p) 



        
# list of student who plays either cricket or badminton but not both
crk_or_bad = []
for student in crk:
    crk_or_bad.append(student)
for student in bad:
    crk_or_bad.append(student)    
for student in crk_and_bad:
    crk_or_bad.remove(student)
for student in crk_and_bad:
    crk_or_bad.remove(student)

for a in crk_or_bad:
    print("Student who plays either cricket or badminton but not both: ",a)




#number of student who play neither cricket nor badminton 
length1 = len(crk_or_bad)
length2 = len(crk_and_bad)

print("Number of student who play neither cricket nor badminton: ",x-length1-length2)




# list of students who play cricket and badminton but not football
crk_and_bad_not_fb = []
for students in crk_and_bad:
    crk_and_bad_not_fb.append(students)
    if students in fb:
        crk_and_bad_not_fb.remove(students)

for b in crk_and_bad_not_fb:
    print("Students who play cricket and badminton but not football",b)
 

#list of students who play atleast one game 
crk_or_bad_or_fb = []

for students in crk_or_bad:
    crk_or_bad_or_fb.append(students)
for students in crk_and_bad:
    crk_or_bad_or_fb.append(students)    
for i in crk_or_bad_or_fb:
    if (i in fb):
        crk_or_bad_or_fb.remove(i)   
for students in fb:
    crk_or_bad_or_fb.append(students)     
for player in crk_or_bad_or_fb:
    print("Students who play atleast one game: ",player)        



#no. of student who do not play any game
z = len(crk_or_bad_or_fb)
print("Number of student who do not play any game: ",x-z)    



#list of student who play all the games
allgames=[]
for students in crk_or_bad_or_fb:
    allgames.append(students)

for students in allgames:
    if students not in crk:
        allgames.remove(students)
for students in allgames:
    if students not in bad:
        allgames.remove(students)
for students in allgames:
    if students not in fb:
        allgames.remove(students)                
for players in allgames:
    print("Student who play all the games: ",players)
