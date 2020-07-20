def intersection(arrays):
    """
    YOUR CODE HERE
    """

    #Begin Setting up for the hash Table
    cache_intersect = {}
    #Setting up our for loops to loop over the data
    for i in arrays[0]:
        cache_intersect[i] = 1
    #Setting up the double for loop
    #Finding from the first position to the end of the intersection
    for z in arrays[1:]:
        for x in z:
            #if it is in here we are going to add 1
            if x in cache_intersect:
                cache_intersect[x] += 1
    #this will show us the length of the array
    list_count = len(arrays)
    #Running out of variable names...
    #We want to check for the items in the cache as well as items being counted
    result = [j for (j, k) in cache_intersect.items() if k == list_count]
    #Ultimately find the intersection
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
