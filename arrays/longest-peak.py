# O(n) time | O(1) space  - where n is the length of the input array
def longestPeak(array):
    longestPeakLength = 0
    peakIdx = 1
    # Iterate through elements in array until we find a peak
    while peakIdx < len(array) - 1: 
        # ======================================
        # STEP 1: Determine the indices of peaks
        # ======================================
        isPeak = array[peakIdx - 1] < array[peakIdx] and array[peakIdx] > array[peakIdx + 1]
        if not isPeak: 
            peakIdx += 1
            continue
        
        # =====================================================================
        # STEP 2: Determine the length of peaks for both sides of the mountain
        # =====================================================================
        # Calculate the left-most index of consecutively decreasing left side of the mountain
        leftIdx = peakIdx - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        
        # Calculate the right-most index of consecutively decreasing right side of the mountain
        rightIdx = peakIdx + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
            
        # Calculate total peak length using the below formula (accounting for zero-indexing)
        currentPeakLength = rightIdx - leftIdx - 1
        # Compare stored longestPeakLength from previous iteration with the curretPeakLength in the current iteration
        longestPeakLength = max(longestPeakLength, currentPeakLength) 
        # Set the peakIdx to be the current interation's right-most index as a starting point to look for the next peak
        peakIdx = rightIdx
        
    return longestPeakLength

myArray = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(myArray))