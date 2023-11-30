"""THIS IS ONLY VALID FOR 3 STUDENT WITH 3 SUBJECTS
            I THINK YOU UNDERSTAND"""

print("What Do You Want :")
print("For New File Type {New}")
print("For Appending Type {Add}")
w=input("\nEnter What Do You Want : ")
if w=="New" or "new":
    f=open("myfile.txt","w")
elif w=="add" or "Add":
    f=open("myfile.txt","a")
else:
    print("Something Wrong!!!")


for p in range(int(input("\nEnter Number Of Students :"))):
    q=(input("\nEnter Marks Of 3 Student Sepreate With Commas :"))
    f.write(f"{q}\n")
f.close()


lis=[]
for s in range(int(input("\nEnter Number Of Subjects(for 3 sub) :"))):
    sub_name=input("Name Of Subjects :")
    lis.append(sub_name)
      
file=open("myfile.txt","r")
i=0
while True:
    i+=1
      
    line=file.readline()    
    if not line:
        break

    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])

    print("\n--------------------\n")
    print(f"\nMarks Of Roll No.{i} in {lis[0]} is:{m1}")
    print(f"Marks Of Roll No.{i} in {lis[1]} is:{m2}")
    print(f"Marks Of Roll No.{i} in {lis[2]} is :{m3}")
    print(line)
    print("\n--------------------")



