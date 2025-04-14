import time
def usingWhile():
    i=0
    while i<50000:
        i=i+1
        print(i)
def usingFor():
    for i in range(50000):
        print(i)
init = time.time() #UsingFor() er kaj shuru houar time
usingFor()
t1 = time.time()-init #kaj sesh er time - kaj shurur time = kaj korte joto time lagse
init = time.time()
usingWhile()
print(time.time()- init)
print(t1)


#    time.sleep()
print("Halar hala")
time.sleep(5) #5sec pore next part print korbe
print("This is printed after 5 seconds")
print("Sayem and Sayeed and Shihab")

#   time.strftime()
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)
