class cat:
    def __init__(self,color,action):
        self.color = color
        self.action = action
    def view(self,num,clr):
        num = num+5
        clr1 = clr
        clr1[0] = "Green"
        print("Method Inside:",num)
        print("Method Inside:",clr1)

#==========================================================================

color = ["Black","Red","Yellow","Blue"]
c1=cat("White","Jumping")
x=55
c1.view(x,color)
print("Method Outside:",x)
print("Method Outside:",color)# Ekhane color[0]="Black" hobe mone holeo Black na hoye Green hoy karon----
'''
#Ekhane x=55 r x er value jokhon class e pass hoy tokhon pass by value hisebe pass hoy tai class er vitore value change holeo
#Mul x er value change hoy na
#tobe color er value clr1 e copy kore er value change korar por o er color er value change hoye geche karon
#color pass hoice Pass by reference e tai color er value pass na hoye color er address tai pass hoye geche tai change hoye geche
#lists, dictionaries, sets, and instances of user-defined classes are passed by reference.
'''