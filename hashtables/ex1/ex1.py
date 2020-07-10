def get_indices_of_item_weights(weights, length, limit):
    # initialize cache
    cache = {}
    # initialize solution
    solution = None
    # iterate throught input weights using index
    for i in range(length):
        # initialize curr_weight
        curr_weight = weights[i]
        # initialize added_weight
        added_weight = limit - curr_weight
        # if limit - weight is not in cache set cache[weight] = index
        if added_weight not in cache:
            cache[curr_weight] = i
        # if limit - weight is in cache
        else:
            # if limit - weight is > current weight solution is [cache[limit-weight], index]
            if cache[added_weight] > i:
                solution = [cache[added_weight], i]
            # else solution is [index, cache[limit-weight]]
            else:
                solution = [i, cache[added_weight]]

    return solution