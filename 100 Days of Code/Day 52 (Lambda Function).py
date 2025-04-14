# def double(x):
#     return x*2

def app(fx,value):
    return 6+fx(value)

#uporer kaj ta 1 line e korar jonno lambda function use kora hoy


double = lambda x:x*2 # er mane lambda function, x ney and x er square kore
print(double(5))

cube = lambda y: y*y*y
print(cube(2))

avg = lambda x,y:(x+y)/2
print(avg(3,5))


print("app function Called: ",app(cube,2)) #ekahne function + lambda function (cube) kaj koreche
print(app(lambda x:x*x,5)) #function er vitore function(lambda) use kora jay


            #Nij
def bll(f,valu):
    return 5+f(valu)
print(bll(lambda x:x*x,6))

sul=lambda y: y**2
print(sul(5))
kk= lambda x,y,z:(x+y-z)/2
print(kk(5,2,1))