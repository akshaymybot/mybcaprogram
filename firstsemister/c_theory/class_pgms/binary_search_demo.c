#include <stdio.h>

int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
 
    while (low <= high) {
        int mid = low + (high - low) / 2;
 
        if (arr[mid] == key)
            return mid;              /* found */
        else if (arr[mid] < key)
            low = mid + 1;           /* search right half */
        else
            high = mid - 1;          /* search left half */
    }
    return -1;                       /* not found */
}
int main(void) {
    int arr[] = {5, 7, 23, 32, 34, 62, 78, 91};   /* must be sorted */
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 62;
 
    int pos = binarySearch(arr, n, key);
 
    if (pos != -1)
        printf("%d found at index %d\n", key, pos);
    else
        printf("%d not found in the array\n", key);
 
    return 0;
}
