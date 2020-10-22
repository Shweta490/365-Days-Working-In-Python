#Python Program For Insertion Sort Algorithm

def insertionSort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        j = i-1
        while(j>=0 and current < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current 
    return arr


if __name__ == "__main__":
    array = [99,4,7,22,1,78,45]

    #calling of insertionSort()
    result = insertionSort(array)
    for each in result:
        print(each,end = " ")
    print()
