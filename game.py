cells_table = [
    ["","",""],
    ["","",""],
    ["","","x"]
]
isBoxTurn = True
selectedCell:int

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

def Is_Position_Valid(pos_to_check:int) -> None :
    """Check if the given position is empty in the table of cells"""
"""
    for elt in cells_table:
        for character in elt:
            if(character == ""):
                
            else:"""
#endregion

def Fill_Cell(isBox:bool) -> None :
    """Check  a box or make a circle in the table of cells with a given position

    Args:
        isBox (bool): Whether the current turn is for box or circle
    """
    # Obtention de la ligne et de la colonne à partir du nombre donné -1, puisque les tableaux commencent à 0
    cells_table[int((selectedCell-1)/3)][(selectedCell-1)%3] = "x" if isBox else "o"
    isBoxTurn = not isBox
    print("Joueur CROIX, à vous !" if isBox else "Joueur CERCLE, let's go !")
    Show_Cells(cells_table)
    NextTurn()

def NextTurn() -> None:
    selectedCell = input("Veuillez entrer une position de 1 à 9 : ")
    try:
        int(selectedCell)
        #Do the other checks here
        #Is_Position_Valid(selectedCell)
    except:
        print("Not a correct position, try again.")
        NextTurn()
    Fill_Cell(isBoxTurn)

############ Initialization of the game ############ 
print("Afin de jouer, entrez une position de 1 à 9.\n"
      "Les positions 1 à 3 correspondent aux cases du haut,\n"
      "les cases 4 à 6 à celles du milieu, etc.")

#Let's say box starts first everytime 
# and it's up to the user to determine who play first

NextTurn()