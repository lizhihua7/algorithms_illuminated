# run time: O(n^2)
# space: O(1)

def selection_sort_0(lst):
    for i in range(len(lst)):
        value_temp = lst[i]
        pos_temp = i
        for j in range(i+1, len(lst)):
            if lst[j] < value_temp:
                value_temp = lst[j]
                pos_temp = j
        lst[pos_temp] = lst[i]
        lst[i] = value_temp
        print(lst)       

if __name__ == '__main__':
    lst =  [13, 16, 18, 4, 10, 7]
    selection_sort_0(lst)