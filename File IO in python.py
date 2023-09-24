     # READING FILE
f=open('myfile.txt','r') #myfile.txt file open hobe and eta read hobe and 'r' na dileo read hoto cz eta default
#print(f)
text=f.read()
print(text)
f.close() # close korte hbe

    #WRITING FILE
x=open('myfile.txt','w') #write mode e nile ager data delete hoye jabe.jodi add korte chai tahole appned mode use korte hbe
x.write("Sorry Abir you are not awesome!")
f.close()

    #APPENDING FILE
x=open('myfile.txt','a')
x.write("Hey Abir try to be a good man.") #Joto bar run korabo toto bar ei line ta add hobe
f.close()


with open('myfile.txt','a') as x: #with diye kaj korle file close kora lage na,auto close hoye jay
    x.write("May Allah bless you.")

'''
                    Modes in file
There are various modes in which we can open files.

1.read (r): This mode opens the file for reading only and gives an error if the file does not exist.
This is the default mode if no mode is passed as a parameter.

2.write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

3.append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

4.create (x): This mode creates a file and gives an error if the file already exists.

5.text (t): Apart from these modes we also need to specify how the file must be handled.
t mode is used to handle text files. t refers to the text mode.
There is no difference between r and rt or w and wt since text mode is the default.
The default mode is 'r' (open for reading text, synonym of 'rt' ).

6.binary (b): used to handle binary files (images, pdfs, etc).

'''