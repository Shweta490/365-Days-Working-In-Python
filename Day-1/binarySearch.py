# Program For Binary Search
# For binary Search operation array must be sorted in ascending Order


def binarySearch(arr,s,l,search):
    """Returns the index of search element if present in array, otherwise returns -1"""
    mid = s+(l-s)//2
    if s<l:
        if search == arr[mid]:
            return mid
        elif search < arr[mid]:
            return binarySearch(arr,s,mid-1,search)
        else:
            return binarySearch(arr,mid+1,l,search)
    else:
        return -1

if __name__ == "__main__":
    arr = list(range(1,100))
    key = 900

    res = binarySearch(arr,0,len(arr),key)
    if res != -1:
        print("{} is present at index: {}".format(key,res))
    else:
        print("{} is not present in the array".format(key)) 
