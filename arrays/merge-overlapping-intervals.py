"""
Input: intervals = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]
Output: output = [[1, 2], [3, 8], [9, 10]]
"""
# O(nlogn) time | O(n) space
def mergeOverlappingIntervals(intervals):
    # Sorting the array of intervals based on the 1st elements of arrays
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    
    mergedIntervals = []
    currentInterval = sortedIntervals[0] 
    mergedIntervals.append(currentInterval) # At least 1 interval is required for the algorithm to work
    
    for nextInterval in sortedIntervals:
        # Decomposing currentInterval into 2 variables (e.g.: currentInterval = [1, 2] gives _ = 1 and currentIntervalEnd = 2)
        _, currentIntervalEnd = currentInterval 
        # Decomposing nextInterval into 2 variables (e.g.: nextInterval = [3, 5] gives nextIntervalStart = 3 and nextIntervalEnd = 5)
        nextIntervalStart, nextIntervalEnd = nextInterval 
        
        # This check determines if two intervals are overlapping by comparing if intervalEnd value of the current interval is bigger or equal than the intervalStart value of the next interval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd) # mutate the currentIntervalEnd to be the highest number between the intervalEnd values of the currentInterval and nextInterval
        else: 
            currentInterval = nextInterval # if there are no overlapping, then immediately append the interval to answer
            mergedIntervals.append(currentInterval)
            
    return mergedIntervals

intervals = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]
print(mergeOverlappingIntervals(intervals))