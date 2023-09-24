import time
t=time.strftime('%H:%M:%S')
print(t)
hour=int(time.strftime('%H'))
print("Hour:",hour)
if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17 ):
    print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
    print("Good Night Sir!")