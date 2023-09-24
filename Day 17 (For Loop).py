
colours=["Red","Green","Blue"]
for kola in colours:
    print(kola)
    for i in kola:
        print(i)
#'''
# Range
for k in range(6):
    print(k)
print("This is a new line")
for k in range(6):
    print(k+1) #k+1 deoar karone 1 theke 6 porjonto print hoice

print("This is a new line")
for k in range(3,9):
    print(k) #3 theke 8 porjonto jabe
print("This is a new line")
for k in range(1000,2001):
    print(k)
print("This is a new line")
for z in range(1,16,3): #3 ontor rekhe songkha print korbe. 3 ekhane jump index
    print(z)


labli="sakin"
for k in labli:
    print(k)
    print(labli)
#for k in labli:


l="Same Work in for loop and while loop"

print(l.center(50,"."))
print("While loop")
num=[12,20,30,40,50]
index=0
suk=0
while index<5:
    print(num[index])
    suk=suk+num[index]
    index=index+1
print("Summation is:",suk)

print("For Loop")
sum=0
for i in num:
    print(i)
    sum=sum+i
print("Summation is:",sum)


colours=["Red","Green"]
for color in colours:
    print(colours)

