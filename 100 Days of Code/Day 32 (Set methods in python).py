s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2)) #AUB orthat A r B er sobgula
s1.update(s2) #er mane s1 er vitor s2 er sokol man dhuke jabe and s1 update ba change hoye jabe.Ekhane print dile None ashbe..
print(s1)
print(s1,s2)
print("\n\n")


cts={'Tokyo','Madrid','Barlin','Delhi'}
cts2={'Tokyo','Seoul','Kabul','Madrid'}
cts3=cts.intersection(cts2) #A∩B orthat A r B er moddeh common gula
print(cts3)
cts.intersection_update(cts2) # intersection hobe and intersection er man cts e dhuke jabe and cts er ager man batil hobe.
print(cts) #New cts = {'Tokyo', 'Madrid'}
cts4=cts.symmetric_difference(cts2) # e khetre common gula bad jabe eta A∩B er ulta
print(cts4)
cts5=cts.difference(cts2) # er mane (cts-cts2)={'Tokyo', 'Madrid'}-{'Tokyo','Seoul','Kabul','Madrid'}
print(cts5)
cts2.difference_update(cts) # (cts2-cts)={'Tokyo','Seoul','Kabul','Madrid'}-{'Tokyo', 'Madrid'} and cts2 cng hoye jabe
print(cts2) #New cts2 = {'Seoul', 'Kabul'}
print(cts.isdisjoint(cts2)) #cts and cts2 er value ekdm alda kina ta dekhbe
print(cts.issuperset(cts2)) #cts2 er sokol value cts er moddeh ache kina ta dekhbe
cts.add("Dhaka")
print(cts)
#2tar kaj same tobe dewoa value na thakle remove ta error korbe and discard ta error show korbe na
print("##cts.remove and cts.discard er kaj:")
cts.remove("Tokyo")
cts.discard("Tokyo")
print(cts)
item=cts.pop()
print(item) #jekono ekta value print korbe and oi value ta cts theke delete hoye jabe
print(cts)
#print(pop)
del cts #cts delete hoye jabe
cts2.clear() # cts2 er sob value clear hoye jabe
print(cts2)