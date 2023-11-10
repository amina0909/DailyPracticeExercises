#lst = [1, 5, 6, 3, 17, 9]

#print(lst[(1+1):])


def replaceElements(arr):
    for i in arr:
        new_arr = arr[i+1:]
        print(new_arr)
        arr[i] = (sorted(new_arr))[-1]
    return arr

replaceElements([17,18,5,4,6,1])
