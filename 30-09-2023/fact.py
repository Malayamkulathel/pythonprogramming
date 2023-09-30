num=int(input("enter a no:"))
factorial=1
if num<0:
    print("factorial doesnt exist for negative no:")
elif num==0:
    print("the factorial of 0 is 1")

else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of",num,"is",factorial)
