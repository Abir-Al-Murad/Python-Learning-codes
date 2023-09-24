#Normally
marks=[12,56,32,60,90,55,45,54]
index=0
for mark in marks:
    print(mark)
    if (index==4):
        print("Kam da korsos ki")
    index +=1

#DOne by Enumerate Function
x="Enumerate Function"
print(x.center(50,"*"))
for index,mark in enumerate(marks): #index,mark er name cng kore dileo 1st er ta index r 2nd ta value e prokash korto
    print(mark)
    if (index==4):
        print("Kam da korsos ki")


print("\nIf you want to start index from 1:\n")
# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for z,o in enumerate(fruits,start=1):
    print(z,o)


print("\nNew System:-\n")
fruits = ['Goaba', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f"{index+1}:{fruit}")