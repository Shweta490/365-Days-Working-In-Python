# Searching Algorithms

**1. Linear Search**

A simple approach is to do a linear search, i.e  <br/>
   a) Start from the leftmost element of arr[] and one by one compare search_key with each element of arr[]<br/>
   b) If search_key matches with an element, return the index.<br/>
   c) If search_key doesn’t match with any of elements, return -1.<br/>


**2.Binary Search**

Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.<br/>

We basically ignore half of the elements just after one comparison.<br/>
   a) Compare search_element with the middle element.<br/>
   b) If search_key matches with middle element, we return the mid index.<br/>
   c) Else If search_key is greater than the mid element, then search_key can only lie in right half subarray after the mid element. So we recur for right half.<br/>
   d) Else (search_key is smaller) recur for the left half.<br/>

*Note - For Binary Search array must be sorted in ascending/descending Order.In the given code in binarySearch.c, We have assumed that array is sorted in ascending Order.


