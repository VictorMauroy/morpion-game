cells_table = [
    ["","",""],
    ["","",""],
    ["","",""]
]
isBoxTurn = True
partyIsOver = False
currentTurn = 0

#region SHOW and CHECK cells
def Show_Cells(cells:list) -> None :
    """Show each cells of the morpion table in the terminal \n
        Also organize the table of cells to print it

    Args:
        cells (list): Table of cells to show
    """
    for elt in cells:
        for character in elt:
            if(character == ""):
                print(" ", end=" ")
            else:
                print(character, end=" ")
        print()

def Is_Position_Valid(line:int, column:int) -> bool :
    """Check if the given line or column is valid : empty or existing

    Returns:
        bool: True if the position is valid, False otherwise
    """
    if cells_table[line-1][column-1] != "" :
        return False
    else :
        return True
#endregion

def NextTurn() -> None:
    selectedLine:int
    selectedColumn:int
    
    selectedLine = input("Quelle ligne ? ==> ")
    try:
        # Do not forget to assign it, otherwise it will not take the int type
        selectedLine = int(selectedLine)
        if(selectedLine < 1 or selectedLine > 3):
            raise IndexError("You are out of range for our cells,"
                         "remind to enter a number between 1 and 3.")
    except:
        print("Ceci n'est pas un numéro de ligne valide.")
        NextTurn()
    
    selectedColumn = input("Quelle colonne ? ==> ")
    try:
        selectedColumn = int(selectedColumn)
        if(selectedColumn < 1 or selectedColumn > 3):
            raise IndexError("You are out of range for our cells,"
                         "remind to enter a number between 1 and 3.")
    except:
        print("Ceci n'est pas un numéro de colonne valide.")
        NextTurn()
    
    if(Is_Position_Valid(selectedLine, selectedColumn)) :
        # Once everything is good, continue !
        Fill_Cell(selectedLine, selectedColumn)
    else :
        print("Cette case est déjà prise.\n"
              "Renseignez à nouveau ligne et colonne.")
        NextTurn()

def Fill_Cell(line, column) -> None :
    """Check  a box or make a circle in the table of cells with 
        a given line and column
    """
    global selectedLine # Set to global to be able to use it here
    global isBoxTurn
    global partyIsOver
    
    cells_table[line-1][column-1] = "x" if isBoxTurn else "o"
    
    # Check if a line of box or circles has been created
    if Check_Line_of_Symbols() :
        partyIsOver = True
        Show_Cells(cells_table)
        print("La victoire appartient au joueur CROIX !" if isBoxTurn 
              else "La victoire appartient au joueur CERCLE !")
    elif currentTurn >= 9 :
        partyIsOver = True
        Show_Cells(cells_table)
        print("Aucun gagnant sur cette partie")
    else :
        isBoxTurn = not isBoxTurn
        Show_Cells(cells_table)
        print("Joueur CROIX, à vous !" if isBoxTurn else "Joueur CERCLE, let's go !")

def Check_Line_of_Symbols() -> bool :
    """Determine if a line of symbols exist by checking around
        the last given position

    Returns:
        bool: True if a line of symbols has been found, False otherwise
    """
    global isBoxTurn
    global currentTurn
    if currentTurn < 5 : # Cannot win before turn 5
        return False
    symbolToCheck = "x" if isBoxTurn else "o"

    if(cells_table[1][1] == symbolToCheck) :
        # If the center cell is filled, we check the 4 possibilities which surrender it
        if cells_table[0][0] == symbolToCheck : # Check diagonal line left > right
            if cells_table [2][2] == symbolToCheck :
                return True
        elif cells_table[0][2] == symbolToCheck : # Check diagonal line right > left
            if cells_table[2][0] == symbolToCheck :
                return True
        elif cells_table[0][1] == symbolToCheck : # Check the vertical line
            if cells_table[2][1] == symbolToCheck :
                return True
        elif cells_table[1][2] == symbolToCheck : # Check the horizontal line
             if cells_table[1][0] == symbolToCheck :
                return True
             
    elif cells_table[0][0] == symbolToCheck :
        #if the cell at the top left is filled, we check 2 possibilities
        if cells_table[1][0] == symbolToCheck : # Check the vertical line
            if cells_table[2][0] == symbolToCheck :
                return True
        elif cells_table[0][1] == symbolToCheck : # Check the horizontal line
             if cells_table[0][2] == symbolToCheck :
                return True
             
    elif cells_table[2][2] == symbolToCheck :
        #if the cell at the bottom right is filled, we check 2 possibilities
        if cells_table[1][2] == symbolToCheck : # Check the vertical line
            if cells_table[0][2] == symbolToCheck : 
                return True
        elif cells_table[2][1] == symbolToCheck :  # Check the horizontal line
             if cells_table[2][0] == symbolToCheck :
                return True
    else :
        return False

############ Initialization of the game ############ 
print("Afin de jouer :\n"
      "Entrez le numéro de la ligne de 1 à 3\n"
      "puis le numéro de la colonne !")
#Let's say box starts first everytime 
# and it's up to the user to determine who play first

while(not partyIsOver) :
    currentTurn+=1
    NextTurn()