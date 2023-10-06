n=str(input("enter the sentence:"))
c=str(input("enter the word you wanna count:"))
d=n.split()
count=0
for i in d:
    if i==c:
        count=count+1
print("number of ",n,"is",count)
