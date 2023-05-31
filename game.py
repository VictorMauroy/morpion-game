cells_table = [
    ["","",""],
    ["","",""],
    ["","",""]
]

def Show_Cells(cells:list) -> None :
    """Show each cells of the morpion table in the terminal

    Args:
        cells (list): Table of cells to show
    """
    for elt in cells:
        print(elt)

Show_Cells(cells_table)