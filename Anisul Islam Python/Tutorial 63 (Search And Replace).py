import re
pattern = r"colour"
text1 = "My favourite colour is Red. I love blue colour as well."
text2 = re.sub(pattern,"Rong",text1,count=1) #count = 1 mane 1st colour lekha k replace kore Rong lekhbe
print(text2)

