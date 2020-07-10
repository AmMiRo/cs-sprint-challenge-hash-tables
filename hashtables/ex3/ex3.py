def intersection(arrays):
    # initialize cache
    cache = {}
    # initialize result
    result = []
    # iterate through arrays with index
    for i in range(len(arrays)):
        # iterate through array in arrays
        for item in arrays[i]:
            # if item not in cache add item to cache with [index] as value
            if item not in cache:
                cache[item] = [i]
            # if item in cache append index to cache[item]
            else:
                cache[item].append(i)
    # iterate through cache
    for key in cache:
        # if length of cache[key] == length of arrays append to solution
        if len(cache[key]) == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
