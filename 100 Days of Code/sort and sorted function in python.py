txt = 'PyNaTive'
lst = list(txt)
lst.sort() #sort,lst er value gulok Capital letter thke Small letter onusare sajay
# lst.sort(reverse=True) #reversed=True dile Choto thke Boro onusare sajabe
txt2 = ''.join(lst)
print(txt2)
#lst.sort() dile original lst change hoye jay
                #Example
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()  # Sorting in ascending order(Choto theke boro kromanosare)
print("Done by sort():",numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

numbers.sort(reverse=True)  # Sorting in descending order(Boro theke choto kromanosare)
print("Done by sort()+reversed:",numbers)  # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]


#sorted() e original lst change hobe na...Notun variable e likha hoy
numbers = [3,2,5,61,49,1,9,6,5]
modified_numbers = sorted(numbers)
print("Done by sorted() function:",modified_numbers)