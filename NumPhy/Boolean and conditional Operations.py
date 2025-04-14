import numpy as np

a = np.array([0,3,4])

#!----Where Condition------
#np.where(condition,x,y) -> if true return x,otherwise y
print(np.where(a>3,1,0))

#!-----Any----
#Kono ekta value non-zero(True) kina check korbe
print(a)
print(np.any(a))
print("Jekono ekti value ki 3 theke boro? -> ",np.any(a>3))

#!-----All-----
#All element non-Zero(True) ki check korbe
print(np.all(a))
print("Shob Value ki 5 thek choto? ->",np.all(a<5))