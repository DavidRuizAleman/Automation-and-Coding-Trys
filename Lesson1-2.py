print ("Welcome to Mysterious House!\n\n")
name = input("What is your name? ").strip().title()

print ('''You are in the *foyer*.  There is a mirror on the wall.  In the mirror,
it says in blood (or possibly ketchup, if you're squeamish\n\n''' + \
  name[::-1].upper() + ''' 
      
	creepy.   Very creepy.  And MYSTERIOUS!

There is a door''')
ans = input('go (through the door) or stay? ')
if ans == 'go':
    print ('''you are in a dark hallway.  It's creepy, but there is \
    a delicious smell from down the hall.  You go towards it.  
    
    The lit room at the end of the hall is a kitchen.   You're ravenous.
    There is a cake on the table. 
    ''')
    ans = input("eat the cake (yes or no)? ")
    if ans == "eat" or ans == "yes":  
        print ("mmmm.... delicious cake")
        ans = input( '''You feel guilty.  Choose a reason:  
        
a.  it's rude to eat someone else's cake
b.  you ate earlier, and were still pretty full
c.  you're allergic to cake\n\n''')
        if ans=='a':
            print ("You're right, it is rude")
        elif ans=='b':
            print ("Well, it's not like there is tupperware around to take it for later")
        else:
            ans = input( "Oh no!  What kind of allergy?  [gluten or anaphalectic]? " )
            if ans[0] == 'g':
                print ('''THE ORACLE PREDICTS.... soon you will need to find a Mysterious........... 


         bathroom.
''')
    else:  # no cake
        print ('''No cake?  REALLY!  Instead you drink beer, pass out, and \
            are eaten by a grue''')
    
else:   # no door
    ans = input('yes or no? ')
    if ans == 'yes':
        print ('''I see you are a person of action!  Too bad you're hanging about in \
a foyer!''')
    else:
        print ('''I sometimes get that way in the winter too''')

print ("\n\nThank you for playing,", name)