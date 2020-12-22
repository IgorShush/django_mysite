def quicksort(alist, start, end):
    '''Sort the list from indexes start to end - 1 inclusive'''

    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while(i <= j and alist[i] <= pivot):
            i = i + 1
        while(i <= j and alist[j] >= pivot):
            j = j - 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j

def logger(msg):
    def log_message():
        print("log: " + msg)
    return log_message