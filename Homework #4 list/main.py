myUniqueList = []
myLeftovers = []

def addUniqueToList(item):
    if item not in myUniqueList:
        myUniqueList.append(item)
        return True
    addLeftovers(item)
    return False
    
def addLeftovers(item):
    myLeftovers.append(item)
    
addUniqueToList(2)
addUniqueToList(5)
addUniqueToList([])
addUniqueToList(3)
addUniqueToList(2)
addUniqueToList(9)
addUniqueToList("o")
addUniqueToList("a")
addUniqueToList("o")
addUniqueToList([])

print("My Unique List ->",myUniqueList)
print("Leftover List ->",myLeftovers)