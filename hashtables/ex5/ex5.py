
def finder(files, queries):
    # initialize cache
    cache = {}
    # initialize result
    result = []
    # iterate through files
    for file in files:
        # initialize split file
        file_name = file.split("/")[-1]
        # if split -1 in cache append cach[split -1] with path
        if file_name in cache:
            cache[file_name].append(file)
        # else add split -1 to cache wit [path] as value
        else:
            cache[file_name] = [file]
    # iterate through queries
    for query in queries:
        # if query in cache iterate through cache[query] to append paths to result
        if query in cache:
            for i in cache[query]:
                result.append(i) 

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
