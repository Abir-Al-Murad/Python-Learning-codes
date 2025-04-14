with open ("file.txt",'r') as f: # 'r' mane read mode e khola hoyeche
    print(type(f))
    #Move to the 10th byte in the file
    f.seek(10)
    print(f.tell()) #koto byte porjonto seek hoice ta bole dibe

    #Read the next 5 bytes
    data = f.read(5)
    print(data)

with open("simple.txt",'w') as t:
    t.write("Hello World")
    t.truncate(5) # simple.txt er 1st 5bytes porjonto print korbe
with open("simple.txt","r") as t:
    print(t.read())