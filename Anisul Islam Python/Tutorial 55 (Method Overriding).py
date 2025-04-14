class phone:
    def __init__(self):
        print("I am in phone class")
class samsung(phone):
    #init
    # pass
    def __init__(self): #phone er init function thaka sotteo abr init use kora k method override bole
        super().__init__() #super class er init print korte hole eta korte hobe
        print("I am in Samsung Class")
s = samsung()
