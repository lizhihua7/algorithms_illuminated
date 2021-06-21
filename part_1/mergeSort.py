# mergeSort algorithm

def divide_list(l):
    if len(l) <= 1:
        return l
    else:
        mid_point = len(l)//2
        l1 = divide_list(l[:mid_point])
        l2 = divide_list(l[mid_point:])
        return merge_sort(l1,l2)

def merge_sort(l1,l2):
    i,j = 0,0
    result = list()
    while i<len(l1) and j<len(l2): # example: if l1 is out of range, that means all l1 is all examined, the rest of l2 can be appended directly to result because l2 is already sorted.
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result += l1[i:] #does not matter l1 or l2 comes first, because they are both sorted, and one of them must be empty(end of the index because of while loop)
    result += l2[j:]
    return result



l = [5,4,1,8,7,2,6,3,9,9,10]
if __name__ == "__main__":
    print(divide_list(l))