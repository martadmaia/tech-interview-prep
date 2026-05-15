# Given an array of intervals where 
# intervals[i] = [starti, endi], 
# merge all overlapping intervals, 
# and return an array of the non-overlapping 
# intervals that cover all the intervals in the input.

#So what's useful here is sorting all the intervals first.
#That way I can compare my current interval only with the previous one
#I should sort by the first element of the interval
#That way, I'll have
#[[2, 4], [8, 10], [3, 6]]

#There's an overlap with with the first and last interval, right?
#When merged, I should get [2, 6]
#So if I sort them, I can compare [3,6] with [2,4], and I know I automatically catch the overlap

#I should also keep an output array, and instead of iterating over the list, and keeping track of indexes and what not, I can just compare my current array with the array that was last modified in the results array.
#I know that output[-1] will either 1) have a merged array, 2) have an unmerged array, that I still need to compare to my current array.


def merge(intervals):
    #first I'll sort the input array, by the first element
    #Complexity O(nlogn)

    intervals.sort(key = lambda array : array[0])

    #I start not with an empty array, but I place the first interval there, 
    #I know I'll need to compare something with it, so I won't waste an iteration
    
    output = [intervals[0]]

    #For comparing
    #I need to check whether my current interval starts at a number 
    #that's lesser than the end of the last placed interval in output
    #Example: current interval [2, 6]
    #If I have [1, 3] in my ouput array, then 2 is clearly < 3.
    #Meaning that array ends "after" my current array starts. Overlap!

    for start, end in intervals[1:]:
        #for comparing them
        if start <= output[-1][1]: #<= because it's in the description [1, 3],  [3, 5] => [1, 5]
            output[-1][1] = max(end, output[-1][1]) #max because I need to know which is going to be the end of my merged interval
        else:
            output.append([start, end])

    return output
             
        
    

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(merge(intervals))    