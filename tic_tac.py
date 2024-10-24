
def printBoard():
    print()
    print(xState[0] ,"|",xState[1] ,"|",xState[2])
    print(f"--|---|--")
    print(xState[3] ,"|",xState[4] ,"|",xState[5])
    print(f"--|---|--")
    print(xState[6] ,"|",xState[7] ,"|",xState[8])
    print()
    
def checkWin(xState):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if xState[win[0]] == "X" and xState[win[1]] == "X" and xState[win[2]] == "X":
            print("X Won the match")
            return 1
        elif xState[win[0]] == "O" and xState[win[1]] == "O" and xState[win[2]] == "O":
            print("O Won the match")
            return 1
    #if any integer is not present in xStates[] it means all posiotions are occupied and it is draw  
    drawCheck = 0
    for i in xState:
        if type(i) == int:
            drawCheck=1
    if drawCheck==0:
        print("Match is Draw")
        return 1
    
    return -1

if __name__ == "__main__":
    xState = [0,1,2,3,4,5,6,7,8]
    turn = True # True for x and False for O
    print("Welcome to Tic Tac Toe")

    while (True):
        printBoard()
        if turn:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            while value>8:
                    value = int(input("Entered value is greater than '8' Please enter the value again :"))
            overlap=True # check if X or O is already present at value entered
            while overlap:
                print()
                if xState[value]=="X":
                    while xState[value]=="X":
                        print("'X' is already at this place")
                        value=int(input("Please  enter another value :"))
                        while value>8:
                            value = int(input("Entered value is greater than '8' Please enter the value again :"))
                    continue

                if xState[value]=="O":
                    while xState[value]=="O":
                        print("'O' is already at this place")
                        value=int(input("Please  enter another value :"))
                        while value>8:
                            value = int(input("Entered value is greater than '8' Please enter the value again :"))
                    continue
                overlap=False
            xState[value] = "X"
        else:
            print("O's Chance")
            value = int(input("Please enter a value:  "))
            while value>8:
                    value = int(input("Entered value is greater than '8' Please enter the value again :"))
            overlap=True
            while overlap:
                if xState[value]=="X":
                    while xState[value]=="X":
                        print("'X' is already at this place")
                        value=int(input("Please  enter another value :"))
                        while value>8:
                            value = int(input("Entered value is greater than '8' Please enter the value again :"))
                    continue

                if xState[value]=="O":
                    while xState[value]=="O":
                        print("'O' is already at this place")
                        value=int(input("Please  enter another value :"))
                        while value>8:
                            value = int(input("Entered value is greater than '8' Please enter the value again :"))
                    continue
                overlap=False
            xState[value] = "O"
        ch=checkWin(xState)
        if ch != -1:
            print(" Mach Over")
            break
        turn = not turn

