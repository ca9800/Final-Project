
alpha = ["A","B","C","D","E","F","G","H","I"]
sunk1 = 0
sunk2 = 0

#######Player 1 Functions

#takes shiplength, coordinates of starting position, and the direction 
def placeShips1(shipL, start, direct):
    if direct == "R": #if the direction is right then...
        for x in range(0, shipL): #builds a ship from left to right starting at that coordinate 
            SP1[start[0]][start[1]+x-1] = 1 #lays down a number of markers acoording to shipL in R direction
            shipList1[5-shipL][x] = str(str(start[0])+str(start[1]+x-1)) #records the ships coordinates in shiplist
            #PRINTING(SP)
    #does the same as above function but for downward direction 
    elif direct == "D":
        for x in range(0, shipL):
            SP1[start[0] + x][start[1] - 1] = 1
            shipList1[5-shipL][x] = str(str(start[0]+x)+str(start[1]-1))
            #PRINTING(SP)
            
#takes a target (like A1) 
def ShootSeeSink1(target):
    
    #convert the (A1) into a coordinate
    Target = list(target)
    Target = [alpha.index(Target[0]), int(Target[1])-1]
    
    HIT = SP1[Target[0]][Target[1]] #accesses player 1's board and sees if there's a ship in the given coordinate
    target = str(str(Target[0])+str(Target[1])) #???
    a=[] #empty list a
    Sunk = sunk1 #keeps track of total # of ships sunk
    if HIT == 1: # if the hit is sucessful then...
        for x in shipList1: #finds which ship was hit
            try: 
                a = [shipList1.index(x), (x.index(target))] #goes to each ship and sees if it was hit to find the ship that was actually hit
            except ValueError: #if the guess produces an error (happens when it "asks" a ship that wasn't hit if it was hit
                print() #if doesn't find anythign prints nothing
        shipList1[a[0]][a[1]] = "H"  #logs the ship that was actually hit  and records it with an H
        print("Hit")
        
        if len(set(shipList1[a[0]])) == 1: #looks for if an entire ship was sunk by seeing if the lenght of set = 1, then that means that the entrie ship was sunk
            print("You sunk my battleship") 
            return(1) #assigns the output of the function as sunk 
        else: return(0) #assigns the output of the function as nothing was hit
    else: 
        print("Miss") #assignes the output of the function as a miss
        return(0) #assigns the output of the function as nothing was hit
    
#Player 2 Functions
#same as player 1 function but accesses player 2's records
def placeShips2(shipL, start, direct):
    if direct == "R":
        for x in range(0, shipL):
            SP2[start[0]][start[1]+x-1] = 1
            shipList2[5-shipL][x] = str(str(start[0])+str(start[1]+x-1))
            #PRINTING(SP)
    elif direct == "D":
        for x in range(0, shipL):
            SP2[start[0] + x][start[1] - 1] = 1
            shipList2[5-shipL][x] = str(str(start[0]+x)+str(start[1]-1))
            #PRINTING(SP)

def ShootSeeSink2(target):
    Target = list(target)
    Target = [alpha.index(Target[0]), int(Target[1])-1]
    HIT = SP2[Target[0]][Target[1]]
    target = str(str(Target[0])+str(Target[1]))
    a=[]
    Sunk = sunk2
    if HIT == 1:
        for x in shipList2:
            try: a = [shipList2.index(x), (x.index(target))]
            except ValueError:
                print()
        shipList2[a[0]][a[1]] = "H"

        print("Hit")
        
        if len(set(shipList2[a[0]])) == 1:
            print("You sunk my battleship")
            return(1)
        else: return(0)
    else: 
        print("Miss")
        return(0)
    

#initializes board for p1        
SP1 = [
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]

#initializes board for p2     
SP2 = [
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]
    
#ship list for P1
shipList1 = [[0,0,0,0,0], [0,0,0,0], [0,0,0], [0,0,0], [0,0]]
#ship list for P2
shipList2 = [[0,0,0,0,0], [0,0,0,0], [0,0,0], [0,0,0], [0,0]]

#keeps track of the various ship lengths for both players
shipLength = [5, 4, 3, 3, 2]

#prints the board 
def PRINTING(board):
    print(" ", [1,2,3,4,5,6,7,8,9])
    T=0
    for x in board:
        print(alpha[T], x)
        T += 1

######Place Ships Player 1

#goes through shiplength list and asks for where the plater wants to pace each ship
for x in shipLength:
    posit = input("Player 1, please input a coordinate for your "+str(x)+" battleship: ") #asks for position
    orient = input("Player 1, please input its orientation (type 'D' for down and 'R' for right) ") #asks for orientation
    
    #convert the inputs form string to coordinates
    posit = list(posit)
    print("HERE IT COMES!!!")
    posit = [alpha.index(posit[0]), int(posit[1])] #should get back a # corresponding to the letter ex B
    
    placeShips1(x, posit, orient) #calls function that actually places the ships
    PRINTING(SP1)

for x in shipLength:
    posit = input("Player 2, please input a coordinate for your "+str(x)+" battleship: ")
    orient = input("Player 2, please input its orientation (type 'D' for down and 'R' for right) ")
    posit = list(posit)
    posit = [alpha.index(posit[0]), int(posit[1])] #should get back a # corresponding to the letter ex B
    placeShips2(x, posit, orient)
    PRINTING(SP2)


    
while sunk1 < 5 or sunk2 < 5: #says while all 5 ships for either player havn't sunk
    
    #player 1 is shooting at player 2
    input ("player 1's turn. Please input your guess. Hit enter to select your target") #has to hit enter because thats what the inputs makeing you do
    shot1 = str(input())
    hit1 = ShootSeeSink2(shot1) #inputted cordinate 
    sunk1 += hit1
    
    #player 2 is shooting at player 1
    input ("player 2's turn. Please input your guess")
    shot2 = str(input())
    hit2 = ShootSeeSink1(shot2)
    sunk2 += hit2












