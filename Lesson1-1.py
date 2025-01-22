## anything from '#' is a comment, and gets ignored.  
## all my editorial comments will start with '##' -- GRL
 
## some text describing what this is
# a simple choose your own adventure
 
## 'print' prints to the screen.  
print ("Welcome to MYSTERIOUS MANSION.")
 
print ("You are at a mysterious door.  The door is clearly marked -- 'Open Me And Die!'."  )
 
## in python, strings can be single or double-quoted
print ('Do you want to open the door?')
 
## raw_input gets input from the user
## Here, we take the input, and *assign* it to a variable called 'ans'
ans = input("please type 'yes' or 'no' ")
 
## conditionals
## see if the user's answer is interesting or not
if ans=="yes":
    print ("That was foolish!  You are now dead.")
## elif means "else-if"
elif ans == "no":
    print ("That was wise!  You are alive, but thoroughly bored.")
## else is a 'catch-all' for "any condition not all ready covered"
else:
    print ("I don't know what to do, based on what you said, which was, |", ans, "|")
 
print ("Thank you for playing!")