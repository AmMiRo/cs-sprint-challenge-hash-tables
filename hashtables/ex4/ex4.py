def has_negatives(a):
    # initialize cache
    cache = {}
    # initialize result
    result = []
    # iterate through a
    for i in a:
        # if item less than 0
        if i < 0:
            # if absolute item in cache append result with absolute item
            if abs(i) in cache:
                result.append(abs(i))
            # else add item to cache with value of True
            else:
                cache[i] = True
        # if item greater than 0
        elif i > 0:
            # if item - item * 2 in cache append result with item
            if i - i * 2 in cache:
                result.append(i)
            # else add item to cache with value of True
            else:
                cache[i] = True

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
