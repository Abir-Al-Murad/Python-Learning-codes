'''
def average(a,b):
    print("Average is = ",(a+b)/2)
a=9
b=2
average(a,b)
'''
#Abar
def average(a=9,b=6):
    print("Average is = ",(a+b)/2)
average()
average(3,2)
average(6) #a=6 hobe and b er man ager tai thakbe
average(b=9) # a er man ager tai thakbe b=9 hoye jabe




def name(a,b,c):
    print("Hello",a,",",b,"and", c)
name('kobita','bobita','lal')



def name(mname,fname='labib',kname="kabir"):
    print("hello",fname,mname,kname)
name("sakib")



def large(a,b):
    if a>b:
        return a
    else:
        return b
print("So Large Number is:",large(40,30))
x=large(60,70)
print("Evabeo same kaj kora jay,So large number is:",x)





