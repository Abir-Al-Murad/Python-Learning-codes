class cat:
    def __init__(self,color,action):
        self.color = color
        self.action = action
    def view(self):
        print(self.color,"Cat is",self.action)
    def compare(self,ct):
        if self.action == ct.action:
            print('Both cats are',ct.action)
        else:
            print("They are different")

#==========================================================

c1 = cat("white","Jumping")
c2 = cat("Brown","Jumping")
c1.view()
c2.view()
c1.compare(c2)
'''
ekhane c1 holo self.action er self and ct.action er ct holo c2
'''