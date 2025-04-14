a=3 #a= None
b=3 #b= None diye a is b dile True ashbe
print(a is b) #exact location of object in memory
print(a==b) #value
# uporer 2ta print e true hobe cz python 2ta variable er man constant(Immutable) houay 2ta k same location e rakhbe r alada korbe na
print("***New Line***")
a=[1,2,55]
b=[1,2,55]
print(a is b) #false ashbe cz eta vinno vinno location e jabe ,,a,b jodi iphone hoy a to r b na mane vinno phone
print(a==b) # eta true ashbe cz value same,,,a,b iphone hole a r b er model same tai true ashbe
tuple = (1,2,6)
tuple1 = (1,2,6)
print(tuple is tuple1) # true ashe cause tuples are immmutable + strings are immutable
print(tuple == tuple1) #true ashbe cz value same
print("*****String Diye****(strings are immutable)")
x= "Labib"
y= "Labib"
print(x is y)
print(x == y)
