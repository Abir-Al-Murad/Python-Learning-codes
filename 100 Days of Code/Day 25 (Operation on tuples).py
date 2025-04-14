countries=("Spain","Italy","India")
print(type(countries))
temp=list(countries) #countries er value gulo temp namok list a rakha hoyeche
temp.append("Bangladesh")
print(temp)
temp.pop(2) #index 2 er value remove kore felbe
print(temp)
temp[2]="Finland" #index 2 e finlad add hobe and Bangladesh remove hobe
countries=(temp) # Countries will become a list though countries is a tuple,cz temp is a list
countries = tuple(temp) # Now Countries is a tuple
print("Hello->",countries)


tuple=(0,1,2,3,2,3,1,3,2)
res=tuple.count(3)
print(res)
