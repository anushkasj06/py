import random
l=["rock","scissor","paper"]


while True:
    ccount =0
    ucount=0
    uc=int(input('''
Game Start...
1 Yes
2.No                 
'''))
    if uc==1:
        for a in range(1,6):
            userInput = int(input('''
1.Rock
2.Scissor
3.Paper                                                                   
'''))
            if userInput == 1:
                uchoice ="rock"
            elif userInput ==2:
                uchoice ="scissor"
            elif userInput==3:
                uchoice = "paper"
            else:
                uchoice="wrong choice"
            Cchoice=random.choice (l)
            if Cchoice == uchoice:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice =="rock" and Cchoice=="scissor")  or  (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("You win") 
                ucount = ucount +1
            else:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Computer Win") 
                ccount = ccount +1
        if ucount==ccount:
            print("Final Game Draw...") 
            print("User Score",ucount)
            print("Computer Count",ccount) 
        elif ucount > ccount:
            print("Final You win The Game...")
            print("User Score",ucount)
            print("Computer Count",ccount)
        else:
            print("Final Computer win the Game...")  
            print("User Score",ucount)
            print("Computer Count",ccount)  



    else:
        break