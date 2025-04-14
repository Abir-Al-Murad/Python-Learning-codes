class employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name in {self.name}")

class dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")

class dancerEmployee(employee,dancer): #eikahen dancer age dile o.show() er jonno dancer class er show function kaj korto
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name

o = dancerEmployee("Kathak","Pritha")
print(o.name)
print(o.dance)
o.show()
print(dancerEmployee.mro()) #mro() - kono method jodi thake seta kothay khoja hobe ta show kore