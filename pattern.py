#pattern 1
for i in range(1,5):
    count = 65

    for j in range(1,i+1):
        print(chr(count),end=" ")
        count=count+1
    print()