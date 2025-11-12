s=input("enter string")
i=0
for x in s:
    print("positive string {} and negative string {} is {}".format(i,i-len(s),x))
    i=i+1