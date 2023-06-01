cells_table = [
    ["","",""],
    ["","",""],
    ["","",""]
]
isBoxTurn = True

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

def Is_Position_Valid(pos_to_check:int, isLine:bool) -> None :
    """_summary_

    Args:
        pos_to_check (int): _description_
        isLine (bool): _description_
    """
    print()
#endregion

def Fill_Cell(line, column) -> None :
    """Check  a box or make a circle in the table of cells with 
        a given line and column
    """
    global selectedLine #Mettre en global pour pouvoir utiliser une variable extérieure
    global isBoxTurn

    # Well, old code without the coordinates system but sorry, I found it interesting
    # cells_table[int((selectedLine-1)/3)][(selectedLine-1)%3] = "x" if isBoxTurn else "o"
    
    cells_table[line-1][column-1] = "x" if isBoxTurn else "o"
    isBoxTurn = not isBoxTurn
    print("Joueur CROIX, à vous !" if isBoxTurn else "Joueur CERCLE, let's go !")
    Show_Cells(cells_table)
    NextTurn()

def NextTurn() -> None:
    selectedLine:int
    selectedColumn:int
    selectedLine = input("Quelle ligne ? ==> ")
    try:
        # Ne pas oublier d'assigner pour que selectedCell prenne un type "int"
        selectedLine = int(selectedLine)
        #Do the other checks here
        #Is_Position_Valid(selectedLine, True)
    except:
        print("Ceci n'est pas une ligne valide.")
        NextTurn()
    
    selectedColumn = input("Quelle colonne ? ==> ")
    try:
        selectedColumn = int(selectedColumn)
        #Is_Position_Valid(selectedColumn, False)
    except:
        print("Ceci n'est pas une cellule valide.:\n"
              "Renseignez à nouveau ligne et colonne.")
        NextTurn()
    # Once everything is good, continue !
    Fill_Cell(selectedLine, selectedColumn)

############ Initialization of the game ############ 
print("Afin de jouer :\n"
      "Entrez le numéro de la ligne de 1 à 3\n"
      "puis le numéro de la colonne !")

#Let's say box starts first everytime 
# and it's up to the user to determine who play first

NextTurn()