def insertion_sort_0(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        while i > 0 and lst[i-1] > key:
            temp = lst[i-1]
            lst[i-1] = key
            lst[i] = temp
            i = i - 1
            print(lst, '\n')

if __name__ == '__main__':
    lst_0 = [5,2,4,6,1,3]
    insertion_sort_0(lst_0)