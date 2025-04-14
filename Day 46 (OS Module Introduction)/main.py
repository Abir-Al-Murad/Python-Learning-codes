import os
if (not os.path.exists("data")): #jodi data name e directory exists na kore tahole data nam e directory khulo
    os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Day {i}") #data directory te day{i+1} nam e file khulo