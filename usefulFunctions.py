indexList = [0]

def findSpecificIndexes(file, target):
    
    if target not in file:
        indexList.pop(0)
        indexList[0] = indexList[0] - 1
        return indexList
    
    else:
        index = file.index(target)
        indexList.append(index + indexList[-1] + 1)

        return findSpecificIndexes(file[index+1:], target)