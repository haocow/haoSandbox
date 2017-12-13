def mergeSort(arr):
    return mergeSortRec(arr[0:len(arr)/2], arr[len(arr)/2:len(arr)])

def mergeSortRec(arr1, arr2):
    print (arr1, arr2)

    if len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1
    else:
        return merge(
            mergeSortRec(arr1[0:len(arr1)/2], arr1[len(arr1)/2:len(arr1)]),
            mergeSortRec(arr2[0:len(arr2)/2], arr2[len(arr2)/2:len(arr2)])
        )

def merge(arr1, arr2):
    arr = []

    while len(arr1) > 0 or len(arr2) > 0:
        if len(arr1) == 0:
            arr += arr2
            break
        elif len(arr2) == 0:
            arr += arr1
            break
        else:
            if arr1[0] <= arr2[0]:
                arr.append(arr1.pop(0))
            else:
                arr.append(arr2.pop(0))

    return arr


print mergeSort([1,3,5,6,4,9,7,2,8])