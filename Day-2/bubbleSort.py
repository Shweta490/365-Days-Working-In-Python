#Python Program to implement Bubble Sort

def bubbleSort(arr):
    for i in range(len(arr)):
        for index in range(len(arr)-i-1):
            if arr[index] > arr[index+1]:
                arr[index],arr[index+1] = arr[index+1],arr[index]
    return arr

if __name__ == "__main__":
    arr = [5,99,1,5,7,9]
    res = bubbleSort(arr)
    for i in res:
        print(i,end = " ")
    print()
