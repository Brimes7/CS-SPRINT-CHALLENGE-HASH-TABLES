def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    #need to create the hash table of weights&&index or i
    #range creases a sequence of numbers and prints them in sequence
    for i in range(length):
        cache[weights[i]] = i
    #Potential pairs of weights need to be found
    #enumerate method will add a counter to an iterable
    #used in for loops
    for z, weight in enumerate(weights):
        #retieve the target weight
        new_weight = limit - weight
        # This will check the existing weight if its there
        if new_weight in cache:
            new_index = cache[new_weight]
            return(z, new_index) if z > new_index else (new_index, z)

    return None
