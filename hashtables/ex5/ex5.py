# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    file_cache = {}
    result = []

    #need tp create an a path
    for p in files:
        #where will we find the file?
        #NEED TO LOOK AFTER the "/"
        #Checks one integer back to make sure there is a "/"
        file = p.split('/')[-1]
        #if we can actaully find file
        #add file to the locations
        if file in file_cache:
            file_cache[file].append(p)
        #if the file isn't known we need to create new files
        else:
            file_cache[file] = [p]
    #Now we need to check if queries is in the files_cache
    for q in queries:
        #Checking for the query in the cached files
        if q in file_cache:
            #Creating results not the same as result
            results = file_cache[q]
            #This will collapse our lists into one list w double for loop
            #p is the path in the query
            for p in results:
                #This will add the results to the path of FINAL Result
                result.append(p)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
