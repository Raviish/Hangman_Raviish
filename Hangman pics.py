HPics=["""
____________
|          |
|          
|         
|
|         
|
|
|
|
""",
"""
____________
|          |
|          0          
|         
|          
|         
|
|
|
|
""",
"""
____________
|          |
|          0          
|          |
|          
|         
|
|
|
|
""",
"""
____________
|          |
|          0          
|         /|
|          
|         
|
|
|
|
""",
"""
____________
|          |
|          0          
|         /|\\
|          
|         
|
|
|
|
""",
"""
____________
|          |
|          0          
|         /|\\
|          |      
|         
|
|
|
|
""",
"""
____________
|          |
|          0          
|         /|\\
|          |      
|         /
|
|
|
|
""",
"""
____________
|          |
|          0          
|         /|\\
|          |      
|         / \\
|
|
|
|
"""
]
p="yes"
while p=="yes" or p=="yeah":
    print "Hangman"+"\n"+"\n"+"\n"+"\n"
    import random
    wordlist=["hey","where","internet","bed","blanket","cookies","slime","banana","candy","floor",
              "anime","vivify","magician","print","laptop","computer","water","zombie","skeleton","vermont","one","vampire","ethernet","xray","treasure","lol","highevery","near","west","dress","best","next","else","checked","grand","stand","matter","forms","value","area"]
    r = random.randint(1,len(wordlist))
    w=wordlist[r-1]
    status="-"*len(w)
    print status
    h=""
    hangman="hangman"
    nw=0
    while h!="hangman" and status!=w:    
        guess=raw_input("")
        if guess in w:
            i = 0
            for l in w:
                if l == guess:
                    status=status[:i]+guess+status[i+1:]
                i = i+1
            print status
        else:
            h=h+hangman[nw]
            nw=nw+1
            print HPics[nw]
            print status
    if h=="hangman":
        print "You Lost,Loser"
        print "The word is "+w+", did you understand"
    else:
        print "OMG,You Won"
    print "Type yes or no to play again or stop"
    p=raw_input("Do you want to play again") 
else:
    print "It was nice playing with you, from Hangman in the computer"
    print "Actually I want to play again, it's sooooooo fun"

