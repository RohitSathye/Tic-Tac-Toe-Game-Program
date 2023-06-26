#Tic-Tac Game
import time

CharX = "X"
CharY = "O"
Player1_win = False
Player2_win = False
Round = int(0)

List0 = ['00','01','02']
List1 = ['10','11','12']
List2 = ['20','21','22']

gamearray = [List0,List1,List2]

#######################################################################

def PrintArray():
    print(*gamearray, sep = '\n')

########################################################################
    
def InsertChar(row,col,sign):
    
        if(row == 0 and col>=0 and col<3):
            if(List0[col] is not CharY and List0[col] is not CharX):
                List0.pop(col)
                List0.insert(col,sign)
            else:
                print("Position already taken. Select Again")
                PrintArray()
                Deal_with_Incorrect_inputs(sign)
                
        elif(row == 1 and col>=0 and col<3):
            if(List1[col] is not CharY and List1[col] is not CharX):
                List1.pop(col)
                List1.insert(col,sign)
            else:
                print("Position already taken. Select Again")
                PrintArray()
                Deal_with_Incorrect_inputs(sign)
                
        elif(row == 2 and col>=0 and col<3):
            if(List2[col] is not CharY and List2[col] is not CharX):
                List2.pop(col)
                List2.insert(col,sign)
            else:
                print("Position already taken. Select Again")
                PrintArray()
                Deal_with_Incorrect_inputs(sign)
                
        else:
            print("Incorrect Row or Column Input. Select Again")
            Deal_with_Incorrect_inputs(sign)

#########################################################################
            
def Deal_with_Incorrect_inputs(sign):
    
    while(Player1_active == True):
                               
        R1 = int(input("Player 1 enter Row (0/1/2):"))
        C1 = int(input("Player 1 enter Column (0/1/2):"))
        InsertChar(R1,C1,sign)
        break
            
    while(Player2_active == True):
                
        R2 = int(input("Player 2 enter Row (0/1/2):"))
        C2 = int(input("Player 2 enter Column (0/1/2):"))
        InsertChar(R2,C2,sign)
        break

###############################################

def Check_Win_scenario(sign):
    if(List0[0] == List1[0] == List2[0] == sign):        
        return True        
    elif(List0[0] == List0[1] == List0[2] == sign):
        return True 
    elif(List0[0] == List1[1] == List2[2] == sign):
        return True 
    elif(List0[1] == List1[1] == List2[1] == sign):
        return True
    elif(List0[2] == List1[2] == List2[2] == sign):
        return True 
    elif(List0[2] == List1[1] == List2[0] == sign):
        return True 
    elif(List1[0] == List1[1] == List1[2] == sign):
        return True 
    elif(List2[0] == List2[1] == List2[2] == sign):
        return True    
    else:
        return False

###############################################################
    
print("Tic-Tac-Toe Game")
print("Player 1 is 'X'")
print("Player 2 is 'O'")
Player1 = input("Player 1 : ")
Player2 = input("Player 2 : ")

print("Let's start the game",Player1, "and" ,Player2)
print("Every box has been denoted by a number")
print("1st Digit - Row , 2nd Digit - Column")

PrintArray()
print("----------------------------------------")

while(Round < 6):

    Round = Round + 1
    print("Round:" ,Round,"starts")
        
    R1 = int(input("Player 1 enter Row (0/1/2):"))
    C1 = int(input("Player 1 enter Column (0/1/2):"))
    Player1_active = True
    Player2_active = False
    InsertChar(R1,C1,CharX)
    
    Player1_win = Check_Win_scenario(CharX)
    
    if (Player1_win):
        print(Player1.upper()," WINS !! - In Round: ", Round)
        break
    
    PrintArray()
    print("-----------------------------------------------")

    if(Round < 5):
        
        R2 = int(input("Player 2 enter Row (0/1/2):"))
        C2 = int(input("Player 2 enter Column (0/1/2):"))
        Player1_active = False
        Player2_active = True
        InsertChar(R2,C2,CharY)

        Player2_win = Check_Win_scenario(CharY)
        
        if (Player2_win):
            print(Player2.upper()," WINS !! - In Round: ", Round)
            break
        
        PrintArray()
        
        Player2_active = False
        print("-----------------------------------------------")

    if (Round == 5):
        if(Player1_win == False and Player2_win == False):
            print("Game Ended in a DRAW : No winners")
            break

print("Final Play : ")
PrintArray()
input("Press e/E to exit.... ")

print("GAME OVER")
time.sleep(5)

####################################################

    





    

