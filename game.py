cells_table = [
    ["x","","o"],
    ["","x",""],
    ["o","","x"]
]
isBoxTurn:bool
selectedCell:int

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

def Check_Box(position:int, isBox:bool) -> None :
    """Check  a box or make a circle in the table of cells with a given position

    Args:
        position (int): Position of the cell to check
        isBox (bool): Whether the current turn is for box or circle
    """

    isBoxTurn = not isBoxTurn

def NextTurn() -> None:
    selectedCell = input("Veuillez entrer une position de 1 à 9")
    try:
        int(selectedCell)
        #Do the other checks here
    except:
        print("Not a correct position, try again.")
        NextTurn()

print("Afin de jouer, entrez une position de 1 à 9.\n"
      "Les positions 1 à 3 correspondent aux cases du haut,\n"
      "les cases 4 à 6 à celles du milieu, etc.")
isBoxTurn = True
Show_Cells(cells_table)