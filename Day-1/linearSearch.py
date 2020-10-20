#A program Which performs the linear search in given array with a  search element

def linearSearch(arr,search):
    """Returns the index of searched element if present in arr, otherwise return -1"""
    for index,value in enumerate(arr):
        if value == search:
            return index
    return -1

if __name__ == "__main__":
    arr =  list(range(1,101))
    key = 67

    res = linearSearch(arr,key)
    if res != -1:
        print("Index of {} in array is : {}".format(key,res))
    else:
        print("key {} is not present in the Array".format(key)) 
