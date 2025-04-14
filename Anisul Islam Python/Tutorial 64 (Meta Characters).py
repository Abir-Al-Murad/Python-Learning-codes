import re
pattern = r"colo.r" # eikhane . mane . er jaygay jekono character hoite pare
pattern2 = r"Sa..ya$" # ekhane .. er jaygay jekono 2ta word hote pare
                    # $ symbol dara bujhay word ta "a" diye sesh hote hobe
if re.match(pattern,"colocr"):
    print("Matched")
if re.match(pattern2,"Samiya"):
    print("Samiya Matched")
if re.match(pattern2,"Sadiya"):
    print("Sadiya Matched")
else:
    print("Tumi Dabba Marso")

if re.match(pattern2,"Samiya") and re.match(pattern2,"Sadiya"):
    print("Samiya Wants Maruf but Maruf wants Sadiya")


# * (0 or more)
# + (1 or more)
# ? (0 or 1)
import re
pattern3 = r"ab*" #a* means string e 1st letter a,b er songkha 0 ba beshi thakte pare error ashbe na
if re.match(pattern3,"aabaacolourabaaa"):
    print("Matched pattern 3 (ab+)")

pattern4 = r"a+" # 1st letter a hote hobe and (1 or more) hote hobe
if re.match(pattern4,"abir Al murad"):
    print("Matched Pattern 4 (a+)")


pattern5 = r"ice(-)?cream" # mane - o/1 bar ba - na dileo hobe dile 1 bar er beshi dite parbe na
if re.match(pattern5,"ice-cream"):
    print("Matched pattern 5 (-)?")


pattern6 = r"a{1,3}$" # string e a 1 thke 3 ti thkte parbe
if re.match(pattern6,"aaa"):
    print("Matched pattern 6 a{1,3}")