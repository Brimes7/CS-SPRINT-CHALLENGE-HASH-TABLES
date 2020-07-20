def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    #Setting up the Hash Table
    for i in a:
        cache[i] = i
        #Checking to see if its not 0 o negaive
        if i is not None and -i in cache:
            print(i)
            #abs is used to return the absolute value
            #append adds the item to the list
            result.append((abs(i)))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
