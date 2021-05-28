def printer(matrix):
    text = ""
    for row in matrix:
        text += "\n"
        for unit in row:
            text += str(unit)
    print (text)