import re
pattern = r"[aeiou]" #ekhaner j kono ekta character matched holei hobe(surui dike letter match hote hobe
if re.match(pattern,"anjalfjaf"):
    print("Matched")

pattern1 = r"[0-9]"
if re.match(pattern1,"aggg0gkjga"):
    print("Matched")
else:
    print("(Unmatched)0-9 er moddeh ekta songkha string er shurute dile Matched hoto")

pattern2 = r"[A-Z][a-z][0-9]"
if re.match(pattern2,"Ag9ghh"): # serial maintain hote hobe(Capital,Small,digit)
    print("Matched pattern 2")