letter="Hey my name is {} and i am from {}"
name="Murad"
country="Bangladesh"
print(letter.format(name,country))
print(letter.format(country,name)) #ektar jaygay onnota print korbe
letter="Hey my name is {1} and i am from {0}" #tobe evabe indicate kore dile thik vabe print korbe
print(letter.format(country,name))
print(f"Hey My name is {name} and i am form {country} and its working through f-string")
price=50.96666
txt=f"for only{price: .2f} dollars!" #Doshomik er por 2 digit porjonto print korbe
print(txt)
print(f"My name is{{Name}}") #{} soho f string print korte chaile evabe likhte hobe


name1=input("Enter your sister name:")
name2=input("Enter your husband name:")
x=f"My sister name is {name1}.Her Husband name is {name2}"
print(x)
print("It's working through x.format()")
print(x.format(name1,name2))


y=f"This is a string: {2*3}"
print(type(y),y)
