#Python Program For Selection Sort

def selectionSort(arr):
    """Returns the Sorted arr in ascending order"""
    for i in range(len(arr)-1):
        minimum = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        if minimum != i:
            arr[i],arr[minimum] = arr[minimum],arr[i]

    return arr

if __name__ == "__main__":
    arr = [99,3,7,2,65,22]
    sortedArray = selectionSort(arr)
    for i in sortedArray:
        print(i,end=" ")
    print()
