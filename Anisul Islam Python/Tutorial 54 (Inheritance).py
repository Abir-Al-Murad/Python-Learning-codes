class phone:
    def call(self):
        print("You Can Call")
    def message(self):
        print("You Can Message")
class samsung(phone): #samsung class er moddeh Phone class k diye dile...phone er sokol function
    def photo(self):   # --samsung function e input hoye jabe etakei Inheritance bole
        print("You Can Take Photo")

p=phone()
p.call()
p.message()
s=samsung()
s.call()
s.message()
s.photo()
print("Ekhane phone hocche Parent/Super/Base class and Samsung holo Child/Sub/Derive class")
print(issubclass(samsung,phone))
