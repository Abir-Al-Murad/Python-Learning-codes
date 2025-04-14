numbers = [1,2,3,4,5]
while (n:=len(numbers))>0: # n:= mane n=,,eta normally print er vitore = use korte eivabe likha hoy
    print(numbers.pop()) # pop() dile sesh er value print kore and main list hote sesh er value ta remove hoye jay


happy = True
print(happy := False)



#walrus Operator chara korle:
foods = list()
while True:
    food = input("What food do you like?:")
    if food == "quit":
        break
    foods.append(food)
    print(foods)
print(f"Done without walrus operator: {foods}")


#Same kaj WAIRUS operator diye korle:
foods1 = list()
while (food2 := input("WHAT FOOD DO YOU LIKE?:")) != "quit": #etar mane- jodi food2 er value "quit" na hoy tahole foods1 e
    foods1.append(food2)                                   # append koro food2 k and quit hole loop sesh
print("Done by using Walrus operator:",foods1)