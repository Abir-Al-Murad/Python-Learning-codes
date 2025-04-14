l=[11,45,1,2,4,6,1]
print("print(l):")
print(l)
print("l.append():")
l.append(7) #ekhane print kora jabe na,,,korle None return korbe....new line e print(l) korte hobe sekhale 7 add hobe
print(l)
print("l.sort:")
l.sort() #choto theke boro komannoye shajabe....ekhane o print kora jabe na
print(l)
print("l.sort(reverse=True):")
l.sort(reverse=True) #boro theke choto komannoye shajabe...print use kora jabe na
print(l)
print("l.index():")
print(l.index(1)) #kto number index e 1 ache ta print korbe
print("l.count():")
print(l.count(1)) #kotota  1 ache tar songkha print korbe

print("New:")
m=l
m[0]=0
print(l)

print("l.insert():")
l.insert(2,899) # 2 number index e 899 add hobe and ager 2nd index 3 e chole jabe
print(l)

print("l.extend():")
j=[900,1000,1100]
l.extend(j) #er mane j er sokol man l er moddeh dhuke gese and egula l er sesh e add hobe
print(l)

