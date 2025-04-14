sentence = "This is a simple example. This is another example."

# Find the last occurrence of "is"
index1 = sentence.rfind("is")
print(index1)  # Output: 31

#find function e 1st er dik theke jekhane is thakbe tar index show korbe, "This" er is o eikhane dhora hobe
index4 = sentence.find("is")
print(index4) # Output: 2

# Find the last occurrence of "is" within the first 20 characters
index2 = sentence.rfind("is", 0, 20)
print(index2)  # Output: 5

# Find the last occurrence of "example"
index3 = sentence.rfind("example")
print(index3)  # Output: 39

# Find the last occurrence of "test" (not present)
index4 = sentence.rfind("test")
print(index4)  # Output: -1
