'''
The fromkeys() method is a class method that belongs to the built-in dict class in Python.
It is used to create a new dictionary with specified keys and a default value for all the keys.
Different Keyword er jonono default value thakle fromkeys(keys,values) function use kora hoy
'''
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result = dict.fromkeys(employees,defaults)
print(result)
print(result["Kelly"])