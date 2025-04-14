import os
# if(not os.path.exists("data")): #Jodi data name e kono directory na thake tahole data name e ekta directory khulbe
#     os.mkdir("data")
#     for i in range(0,100):
#         os.mkdir(f"data/Day {i+1}") #data directory te Day 1-100 porjonto file khule dibe
# for i in range(0,100):
#     os.rename(f"data/Day {i+1}",f"data/Tutorial {i+1}") #Day 1-100 er name change kore Tutorial 1-100 kore dibe


#file create hoye gese tai comment kore diyechi ta na hole run korle error through korbe


folders=os.listdir("data")
print(folders) #datar moddehr file gula list akare ashbe
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}")) #folder er moddeh kon folder ache ta dekhabe
print(os.getcwd()) #file er location show korbe
os.chdir("/python practice") #file er location change hobe and next kaj oikahen hobe (oikhane hobe kina not sure.)
print(os.getcwd())