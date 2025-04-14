class house:
    def __init__(self,w,d):
        self.window = w
        self.door = d
    def view(self):
        print("The house has",self.window,"Window(s) and",self.door,"Door(s)")
    def __add__(self, other):
        new_window = self.window + other.window
        new_door = self.door + other.door
        obj = house(new_window,new_door)
        return obj
        #return "New house has"+str(new_window)+" windows and
#================================================================================================

h1 = house(6,2)
h2 = house(4,1)
h1.view()
h2.view()
h3 = h1+h2 #h1.__add__(h2)
h3.view()
print(h1+h2) #h1.__add__(h2)