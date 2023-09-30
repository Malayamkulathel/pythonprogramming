a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
c=int(input("enter 3rd no:"))
if(a>=b)and(a>=c):
    largest=a
elif(b>=a)and(b>=c):
    largest=b
else:
    largest=c
print("the largest number is:",largest)
