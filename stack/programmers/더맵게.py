# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
from queue import PriorityQueue
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        answer += 1
    return answer


# 효율성4
# def solution(scoville, K):
#     answer = 0
#     queue = PriorityQueue()
#     for i in range(len(scoville)):
#         queue.put(scoville[i])
#
#     while queue.queue[0] < K:
#         if queue.qsize() < 2:
#             return -1
#         first = queue.get()
#         second = queue.get()
#         queue.put(first + (second * 2))
#         answer += 1
#     return answer


### 정확도 효율성 다 떨어짐
# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#
#     while not allScovilleOverK(scoville, K):
#         if len(scoville) < 2:
#             answer = -1
#             break
#         new_scoville_index = mixFirstAndSecond(scoville)
#         append_new_scoville_index(scoville, new_scoville_index)
#         answer = answer + 1
#     return answer


def allScovilleOverK(scoville, k):
    return scoville[0] >= k


def mixFirstAndSecond(scoville):
    first = scoville.pop(0)
    second = scoville.pop(0)
    new_scoville_index = first + (second * 2)
    return new_scoville_index


def append_new_scoville_index(scoville, new_scoville_index):
    if len(scoville) == 0:
        scoville.append(new_scoville_index)
    for index in range(len(scoville)):
        if new_scoville_index > scoville[index]:
            scoville.insert(index, new_scoville_index)
            break
