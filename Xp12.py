# list=[1,2,2,3,3,4]
# s=set(list)
# print(s)

l=eval(input("enter list"))
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)