arr1 = ['a', 'b', 'c', 'x']
arr2 = ['z', 'y', 'q']

def containsCommonItem(array1, array2):
    itemSet = set()
    for item in array1:
        itemSet.add(item)

    for item in array2:
        if item in itemSet:
            return True;

    return False

print(containsCommonItem(arr1, arr2))