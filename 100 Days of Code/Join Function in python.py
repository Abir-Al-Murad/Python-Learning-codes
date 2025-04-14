lis = ["John","Randy","Sheamus","Khali","Jinder Mahal"]
a = ' and '.join(lis) # and diye sobgulak join koriye dibe
print(a,"Other WWE Superstars")
#jodi faka rakhte chai tahole '' er majhe kisu na dilei hobe

#Qsn-> Given string contains a combination of the lower and upper case letters.
#Write a program to arrange the characters of a string so that all lowercase letters
# should come first.
str1 = "PYnAtiVe"
print("Original String:",str1)
lower = []
upper = []
for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
result = ''.join(lower+upper)
print("Result: ",result)


