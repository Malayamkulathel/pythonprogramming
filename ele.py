list=[]
n=int(input("enter no:of elemenys:"))
for i in range(0,n):
    ele=input("enter colors:")
    list.append(ele)
    print(list)
print("the first and last elements are:",list[0],list[-1])
