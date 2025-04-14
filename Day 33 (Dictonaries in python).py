dic={
    317:"BM Mehedi Hasan",
    318:"Abir Al Murad",
    319:"Sanowar",
    320:"Jabed"
    }
print(dic[318])

info={"name":'Karan','age':21,'eligible':True}
print(info)
print(info["name"]) # eta r nicher ta same kaj kore tobe vul key dile eta error show kore r oita none
print(info.get("name"))
print(info.keys())
print(info.values())
for key in info.keys():
    print(key)
for key in info.keys():
    print(f"The value corresponding to the key {key} in {info[key]}")
print(info["name"])
print(info.items())
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

code={'Day 10':'Taking input','Day 11':'String','Day 13':'Strings Methods'}
print(code.items())
for ckey,cvalue in code.items():
    print(f"In {ckey} we will learn about - {cvalue}")