#Python code for file-handling process
# This is a beginner program
#lets begin

file1=open("myfile.txt","w")
L= ["this is delhi \n","this is paris \n","this is london \n"]
file1.write("hello \n")
file1.writelines(L)
file1.close()
#appends adds at last
file1 =open("myfile.txt","a")
file1.write("today \n")
file1.close()
file1=open("myfile.txt","r")
print("output of readlines after appending")
print(file1.read())
print()
file1.close()
