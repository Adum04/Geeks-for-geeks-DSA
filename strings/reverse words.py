def reverseWords(self, stri):
    lst = stri.split(".")
    n = len(lst)
    low = 0
    high = n - 1
    mid = n // 2
    while low < mid:
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1
    new_str = ".".join(str(i) for i in lst)
    return new_str
