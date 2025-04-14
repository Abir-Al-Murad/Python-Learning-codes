j="VAI VAI QUIZ COMPETITION"
print(j.center(50,"*"))
x='''\n1) Which is the National Mourning Day?
    a)20 August         b)15 September
    c)15 August         d)20 August'''
print(x)
i=0
o=input("Type Your answer: ")
if (o=="c" or o=="15 August"):
    print("Answer is Right.\n")
    i=1
else:
    print("Answer is Wrong.\n")
y='''2) Who is the Prime Minister of Bangladesh?
    a)Khaleda Zia        b)Sheikh Hasina
    c)Hasina Begum       d)Sheikh Mujibur Rahman'''
print(y)
c=input("Type Your Answer:")
if (c=="b" or c=="Sheikh Hasina"):
    print("Answer is Right.\n")
    i=i+1
else:
    print("Answer is Wrong.\n")
z='''3) Which is the National Independence day?
    a)16 December        b)7 March
    c)26 March           d)21 February
'''
print(z)
e=input("Type Your Answer:")
if (e=="c" or e=="26 March"):
    print("Answer is Right.\n")
    i=i+1
else:
    print("Answer is Wrong.\n")
l='''4) Who is the Education Minister of Bangladesh?
    a)Dipu Apa           b)Dipu Moni
    c)Dipu vai           d)Dipu Khala
'''
print(l)
d=input("Type Your Answer:")
if (d=="b" or d=="Dipu Moni"):
    print("Answer is Right.\n")
    i=i+1
else:
    print("Answer is Wrong.\n")
u='''5) Which is the City Of Hilsha?
    a)Dhaka              b)Chattogram
    c)sylhet             d)Chandpur
'''
print(u)
r=input("Type Your Answer: ")
if (r=="d" or r=="Chandpur"):
    print("Answer is Right.\n")
    i=i+1
else:
    print("Answer is Wrong.\n")
print("YOU GOT",i,"OUT OF 5")