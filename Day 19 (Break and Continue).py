a="Break Statement"
print(a.center(50,"."))
for i in range(12):
    if (i==10):
        break
    print("5x",i+1,"=",(5*(i+1)))
b="Continue statement"
print(b.center(50,"."))
for i in range(13):
    if(i==10):
        print("10 Break kore eta print korlam")
        continue
    print("5X",i,"=",5*i)
k="New Code Running"
print(k.center(50,"."))
for i in range(1,101):
    print(i,end=" ")
    if(i==20):
        break
    print("Valobasha")
print("Thank you")
