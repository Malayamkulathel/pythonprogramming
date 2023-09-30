n=int(input("enter the total no: you want to add:"))
sum=0
for i in range(n):
    x=int(input("enter the nos:"))
    sum=sum+x
print("sum:",sum)
avg=sum/n
print("average",avg)
