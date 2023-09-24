countries=("Spain","Italy","India")
temp=list(countries) #countries list e porinoto hobe
temp.append("Bangladesh")
print(temp)
temp.pop(2) #index 2 er value remove kore felbe
print(temp)
temp[2]="Finland" #index 2 e finlad add hobe
countries=tuple(temp) #countries abr tuple e porinoto hobe
print(countries)


tuple=(0,1,2,3,2,3,1,3,2)
res=tuple.count(3)
print(res)
