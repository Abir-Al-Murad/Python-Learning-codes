a=330
b=3303
print("A") if a>b else print("=") if a==b else print("B")
# print("A") jodi a>b hoy r na hole print("=") jodi a==b hoy r na hole print("B")


print(9) if a>b else "" #else er por khali rakha jabe na tai sesh e "" sign dite hbe


c=9 if a<b else ""
print(c)



try:
    x = int(input("Enter the percentage of your battery(1-100):"))
    print("Battery Health is so good.") if (x>=80 and x<=100) else print("Battery Health is OK.") if (x>=50 and x<80) else print("Battery is Low plz Charge your Battery") if (x>=30 and x<50) else print("Your mobile is going to turn off,Connect your charger quickly.")
except:
    print("Please enter valid Number(Integer)")
