#Function chara finally keyword
try:
    l = [1, 5, 36, 4, 8]
    i = int(input("Enter the index:"))
    print(l[i])
    # return 1 #return shudu functin e kaj kore
except:
    print("Some Error Occurred.")
    # return 0
finally:
    print("I am always executed.")






def function1():
    try:
        l=[1,5,36,4,8]
        i=int(input("Enter the index:"))
        print(l[i])
        return 1 #ekbar return hoye gele next jinish gula execute kore na tobe finally keyword kore tai finally keyword use kora hoy
    except:
        print("Some Error Occurred.")
        return 0
    finally:
        print("I am always executed.")

function1()