def sort(arr: iter) -> iter:
    """
    Perform counting sort on the input list 'arr' in-place.

    :param arr: The input list to be sorted.
    :return: arr -- The sorted array.
    """
    sorted_arr = []
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    for val in arr:
        counts[val] += 1
    for i in range(len(counts)):
        for j in range(counts[i]):
            sorted_arr.append(i)

    return sorted_arr


if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = sort(my_list)

    print("Original List:", my_list)
    print("Sorted List:", sorted_list)
