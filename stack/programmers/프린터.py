from operator import itemgetter

def solution(priorities, location):
    nums_with_idx = list(enumerate(priorities))
    print_cnt = 0
    while(nums_with_idx):
        top_priority =max(nums_with_idx, key=itemgetter(1))[1]
        target = nums_with_idx.pop(0)
        if target[1] == top_priority:
            print_cnt += 1
            if target[0] == location:
                break
        else:
            nums_with_idx.append(target)
    return print_cnt

# def solution(priorities, location):
#     nums_with_idx = list(enumerate(priorities))
#     print_queue = []
#     answer = 0
#     while(nums_with_idx):
#         top_priority =max(nums_with_idx, key=itemgetter(1))[1]
#         target = nums_with_idx.pop(0)
#         if target[1] == top_priority:
#             print_queue.append(target)
#         else:
#             nums_with_idx.append(target)
#
#     for idx, print in zip(range(len(print_queue)),print_queue):
#         if print[0] == location:
#             answer = idx + 1
#             break
#
#     return answer