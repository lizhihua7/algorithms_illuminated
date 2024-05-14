# running time: log2 n

def binary_search_0(lst, target):
    step_num = 0
    min = 0
    max = len(lst) - 1
    cur_prime = None
    while cur_prime != target and max >= min:
        step_num += 1
        cur_pos = int((min+max)/2)
        cur_prime = lst[cur_pos]
        if cur_prime < target:
            min = cur_pos + 1
        elif cur_prime > target:
            max = cur_pos - 1
    if max < min:
        cur_pos = -1
    print('target prime position:', cur_pos)
    print('step count:', step_num)

if __name__ == '__main__':
    prime_lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    target = 67
    binary_search_0(prime_lst, target)