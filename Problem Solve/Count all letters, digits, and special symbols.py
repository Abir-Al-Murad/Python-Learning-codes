str1 = "P@#yn26at^&i5ve"
chars = 0
Digits = 0
symbol =0
for i in str1:
    if i.isalpha():
        chars = chars+1
    elif i.isdigit():
        Digits = Digits+1
    else:
        symbol = symbol+1
print("Chars: ",chars)
print("Symbol: ",symbol)
print("Digits: ",Digits)