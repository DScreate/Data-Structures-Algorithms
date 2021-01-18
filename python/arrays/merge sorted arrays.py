def mergeSortedArrays(array1, array2):
    if(len(array1) == 0):
        return array2

    if(len(array2) == 0):
        return array1

    indexOf1 = 0;
    indexOf2 = 0;
    returnList = []
    # iterate through each array with seperate pointers
    # compare each index that the pointers are referencing and push that value into the new array
    # iterate that pointer
    # do this until each pointer is > length of the array -> pointing at nothing
    while(indexOf1 < len(array1) and indexOf2 < len(array2)):
        # do comparison
        if array1[indexOf1] < array2[indexOf2]:
            returnList.append(array1[indexOf1])
            indexOf1+=1
        else:
            returnList.append(array2[indexOf2])
            indexOf2+=1

    while(indexOf1 < len(array1)):
        returnList.append(array1[indexOf1])
        indexOf1+=1

    while(indexOf2 < len(array2)):
        returnList.append(array2[indexOf2])
        indexOf2+=1

    return returnList