class A:
    def __init__(self):
        print("__init__ of class A.")
    def method1(self):
        print("Method1 of class A.")
#===============================================
class B:
    def __init__(self):
        print("__init of class B.")
    def method1(self):
        print("Method1 of class B.")
#=========s=======================================
class C(B,A):
    #def __init__(self):
        #print("__init__ of class of C.")
    '''
    amra jodi c er init method comment kore dei
    tahole kar init mathod call hobe??Class A naki B er??
    jehoto B age tai B er init method call hobe.
    '''
    #Abar
    def __init__(self):
        super().__init__()#ekhetre o B er init call hobe
        '''jodi A er init call dite chai??tahole-->'''
        A.__init__(self)#ekhetre self dite hobe
        print("__init__ of class of C.")
    def method2(self):
        print("Method2 of class C.")
#================================================
c1 = C()
c1.method1() #A and B te same method1 ache, B jehoto age tai B er method1 call hobe
#c1 er reference e A er method1 call-->
A.method1(c1) #class C theke A class er method1 call
c1.method2()