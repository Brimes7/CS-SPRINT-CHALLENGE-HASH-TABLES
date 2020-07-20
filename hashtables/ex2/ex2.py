#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    #Create the hash table
    cachefly = {}
    #Creating the route
    route = [None] * length
    #This check to see which flight is next on our list.
    #if we hit the end early the next flight will be none
    for t in tickets:
        cachefly[t.source] = t.destination
    next = cachefly["NONE"]
    #checks the flights as well starting from 0 the end of route
    for z in range(0, length):
        route[z] = next
        next = cachefly[next]

    return route
