cells_table = [
    ["x","","o"],
    ["","x",""],
    ["o","","x"]
]

def Show_Cells(cells:list) -> None :
    """Show each cells of the morpion table in the terminal

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

Show_Cells(cells_table)