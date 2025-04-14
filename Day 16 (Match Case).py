x=int(input("Enter Tor Hoga: "))
match x:
    case 0:
        print(x,"is zero")
    case 6:
        print("X is six")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=61:
        print(x,"is not 61")
    case _:
        print(x)



status_code=int(input("Enter Your Pacha:"))
match status_code:
    case 400:
        print("Bad Request..!!")
    case 200:
        print("Good Request...!!")
    case _: #space diye underscore use korte hobe
        print("Something else which is bad.")
