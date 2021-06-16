def createBoard(rows,columns):
    if rows > 17 or columns > 148:
        print("The Row value can't be greater than 17 & Column value can't be greater than 148")
        return False
    for row in range(rows):
        for col in range(columns):
            if not col%2 == 0:
                print("|",end="")
            else:
                print(" ",end="")
        print()
        if row < rows-1: 
            print ("-"*columns)
    return True


createBoard(17,148)