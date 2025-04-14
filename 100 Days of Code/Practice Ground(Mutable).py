def fx(x):
    return round(x**3-2*x**2-4,5)
def fx2(x):
    return round(3*x**2-4*x,5)
def xnew(x):
    return round(x-(fx(x)/fx2(x)),5)

x=2
for i in range(1,100):
    if(x==xnew(x)):
        break
    else:
        if i == 5:
            print(fx(x))
            print(fx2(x))
            print(xnew(x))
            print(f"Iteration {i} , x = {x:.5f}")
        else:

            xnew(x)
            x=xnew(x)
            print(f"Iteration {i} , x = {x:.5f}")
