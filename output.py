def printer(matrix):
    text = ""
    for row in matrix:
        text += "\n"
        for unit in row:
            if unit: 
                text += "**"
            else: 
                text += ",,,,"
            #text += str(unit)
    return   (text)