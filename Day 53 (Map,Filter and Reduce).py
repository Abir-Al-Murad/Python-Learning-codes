def cube(x):
    return x*x*x
print(cube(5))
l=[1,2,3,5,9]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)
#same kaj loop diye na kore map diye kora
print("*****MAP*****")
newl=list(map(cube,l)) # (function er nam, list er nam) jetar prottek element er upore function apply korbe
print(newl)
#Cube name e extra function na baniye o eivabe kora jay
i=[2,6,5,8]
pls=list(map(lambda x:x*x*x,i))
print(pls)


#same kaj lambda dara ->
cube1=lambda y:y*y*y #y nibe and y er cube korbe
k=[2,5,2,5]
new=list(map(cube1,k)) # k er prottek value te cube1 function kaj korbe
print(new)

#FILTER
print("********Filter*********")
p=[32,2,5,6,78,55]
def filter_function(a):
    return a>20
newnewl=list(filter(filter_function,p)) #p variable er joto man 20 er beshi, oigula print korbe
print(newnewl)

print("*******REDUCE*******")

from functools import reduce
#list of numbers
numbers=[1,2,3,4,5]
#calculate the sum of the numbers using the reduce function
def mysum (x,y):
    return x+y
sum = reduce(mysum,numbers) #jevabe kaj kore:(numbers hote) 1+2=3,3+3=6,6+4=10,10+5=15
print(sum)
