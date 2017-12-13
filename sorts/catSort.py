def getCat(num):
    if num < 10:
        return 1
    elif num < 20:
        return 2
    else:
        return 3

def catSort(arr):
    cats = {}

    for i in range(len(arr)):
        cat = getCat(arr[i])
        cats[cat] = i

        keys = sorted(cats.keys())
        for j in range(len(keys)-1):
            ind1 = keys[j]
            ind2 = keys[j+1]

            if cats[ind1] > cats[ind2]:
                arrInd1 = cats[ind1]
                arrInd2 = cats[ind2]

                tmp = arr[arrInd1]
                arr[arrInd1] = arr[arrInd2]
                arr[arrInd2] = tmp

                tmp2 = cats[ind1]
                cats[ind1] = cats[ind2]
                cats[ind2] = tmp2

    print cats
    return arr

arr = [21,18,3,2,15]
print arr
print catSort(arr)