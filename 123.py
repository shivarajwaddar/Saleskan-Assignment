n=int(input("Enter number of students:  "))

namearr=[]
# sem1=[]
# sem2=[]
avgsem1=0
avgsem2=0
Englishavgsem1=0
Mathsavgsem1=0
Scienceavgsem1=0
Englishavgsem2=0
Mathsavgsem2=0
Scienceavgsem2=0
allsemavg=[]



for i in range(n):
    
    name=input("Enter student name:  ")
    namearr.append(name)
    marksarrsem1=[]
    marksarrsem2=[]
    print()
    print("Enter sem 1 marks")
    English=int(input("Enter marks of Engish:  "))
    Science=int(input("Enter marks of Science:  "))
    Maths=int(input("Enter marks of Maths:  "))
    marksarrsem1.extend([English,Science,Maths])
    avg1=(English+Science+Maths)/3
    avgsem1+=avg1
    Englishavgsem1+=English
    Scienceavgsem1+=Science
    Mathsavgsem1+=Maths
    # sem1.append(marksarrsem1)
    print()
    
    print("Eneter sem 2 marks")
    English=int(input("Enter marks of Engish:  "))
    Science=int(input("Enter marks of Science:  "))
    Maths=int(input("Enter marks of Maths:  "))
    marksarrsem2.extend([English,Science,Maths])
    avg2=(English+Science+Maths)/3
    avgsem2+=avg2
    Englishavgsem2+=English
    Scienceavgsem2+=Science
    Mathsavgsem2+=Maths
    # sem2.append(marksarrsem2)
    bothsemavg=avg1+avg2
    allsemavg.append(bothsemavg)
    
    print()
    print()


print(namearr)
# print("sem 1 marks: ",sem1)
# print("sem 2 marks: ",sem2)
print()
print("Task1")
print("Avarage percantage of whole class in sem 1 is: ",avgsem1/n)
print("Avarage percantage of whole class in sem 2 is: ",avgsem2/n)
print()
print("Task2")
print("Avarage marks of students in sem 2 in Engish subject is: ",Englishavgsem1/n)
print("Avarage marks of students in sem 2 in Science subject is: ",Scienceavgsem1/n)
print("Avarage marks of students in sem 2 in Maths sujlect is: ",Mathsavgsem1/n)
print("Avarage marks of students in sem 2 in Engish subject is: ",Englishavgsem2/n)
print("Avarage marks of students in sem 2 in Science subject is: ",Scienceavgsem2/n)
print("Avarage marks of students in sem 2 in Maths subject is: ",Mathsavgsem2/n)
print()
print("Task3")
print()
maxm=max(allsemavg)
for i in range(n):
    if(maxm==allsemavg[i]):
        print("The highest scorer in the class is : ",namearr[i],"   With the Avarage marks in each sem is : ", maxm/2)
        
allsemavg.remove(maxm) 
secmax=max(allsemavg) 
for i in range(n-1):
    if(secmax==allsemavg[i]):
        print("The second highest scorer in the class is : ",namearr[i],"   With the Avarage marks in each sem is : ", secmax/2)
             




