#Exercise 3: Print characters from a string that are present at an even index number
str = input('Type your GF name:')
x=len(str)
for i in range(0,x-1,2):
        print(f"Index[{i}]", str[i])
