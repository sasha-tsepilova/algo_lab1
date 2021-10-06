def merge_sort(arr: list):
    '''
    Performs sorting by merge method.
    Returns sorted array and number of comparisons made.
    '''
        
    comp = 0
    n = len(arr)
    if n <= 1:
        return arr, comp

    mid = n//2
    left, right = arr[:mid], arr[mid:]

    res_left = merge_sort(left)
    left = res_left[0]

    res_right = merge_sort(right)
    right = res_right[0]

    comp += res_left[1] + res_right[1]
    left.append(float('inf'))
    right.append(float('inf'))

    ind_left, ind_right = 0, 0
    for i in range(n):
        if right[ind_right] < left[ind_left]:
           arr[i] = right[ind_right]
           ind_right += 1
        else:
            arr[i] = left[ind_left] 
            ind_left += 1
        comp += 1
    
    return arr, comp


def selection_sort(arr: list):
    '''
    Performs sorting by selection method.
    Returns sorted array and number of comparisons made.
    '''
    uns_ind = 0
    n = len(arr)
    comp = 0
    while(uns_ind < n):
        current_min = arr[uns_ind]
        cur_min_ind = uns_ind
        for i in range(uns_ind + 1, n):
            if current_min > arr[i]:
                current_min, cur_min_ind = arr[i], i
            comp += 1
        arr[cur_min_ind] = arr[uns_ind]
        arr[uns_ind] = current_min
        uns_ind += 1

    return arr, comp

def insertion_sort(arr:list):
    '''
    Performs sorting by insertion method.
    Returns sorted array and number of comparisons made.
    ''' 
    comp = 0
    n = len(arr)
    for ind in range(1, n):
        i = ind
        while  i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
            comp += 1
        comp += 1
    return arr, comp

def shell_sort(arr:list):
    '''
    Performs sorting by shell method.
    Returns sorted array and number of comparisons made.
    ''' 
    comp = 0
    n = len(arr)
    gap = 1

    while gap < n/3:
        gap = gap*3 + 1

    while gap >= 1:
        for cur_ind in range(gap, n):
            to_comp = cur_ind
            while(to_comp >= gap and arr[to_comp] < arr[to_comp - gap]):
                comp += 1
                arr[to_comp], arr[to_comp - gap] = arr[to_comp - gap], arr[to_comp]
                to_comp -= gap
            comp += 1
        gap //= 3
    
    return arr, comp
