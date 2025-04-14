cp1={122:45,123:89,567:69,670:69}
cp2={222:67,566:90}
cp1.update(cp2)
print(cp1)
# cp1.clear()
# print(cp1)
cp1.pop(122) #122 key er key soho value remove kore dibe
print(cp1)
#popitem---> Sesh key_value remove kore dibe dictionary hote
cp1.popitem()
print(cp1)
del cp1[567] #567 key er value soho delete hoye jabe
print(cp1)