'''
Regular expressions can be accessed using the re module
match() : matches at the beginning of a string.
search() : finds a match of a pattern anywhere in the string.
findall() : returns a list of all substrings that match a pattern.
'''
#Regular module use korte hole re import korte hobe
import re
pattern = r"Colour"
if re.match(pattern,"Red is a colour, I Love red colour"):
    print("Matched") #eikhane 1st e Red tai not matched ashbe,jodi Colour 1st e ashto tahole Matched hoto
else:
    print("Not Matched")




#Eta Matched hobe cz pattern2 er Colour r if e lekha 1st word colour/c/co/col etc
pattern2 = r"Colour"
if re.match(pattern2,"Colour is Red, I Love red colour"):
    print("Matched")
else:
    print("Not Matched")

#Search Method

pattern3 = r"colour"
if re.search(pattern3,"Red is a colour, I Love red colour"):
    print("Matched") #eikhetre Search method jekono jaygay colour lekha pelei True hobe ba Matched return korbe
else:
    print("Not Matched")

#more on search method
import re
pattern = r"colour"
text = "My favourite colour is Red."
match = re.search(pattern,text)
if match:
    print(match.start()) #kon jaygay colour ache setar index print korbe
    print(match.end()) #colour er sesh word(r) er index number show korbe
    print(match.span()) #uporer 2tar kaj korbe


    
#findall method

pattern4 = r"colour" #col dile colour er col niye list korto
print(re.findall(pattern4,"Red is a colour, I Love red colour, c,co,col"))
#eta string e joto gula colour lekha ache sobgular ekta list kore dibe