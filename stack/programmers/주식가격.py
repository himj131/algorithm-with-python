# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.


# answer 개수 만큼 미리 만들어 놓은 경우 통과
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break
    return answer


# 효율성 0
# def solution(prices):
#     answer = []
#
#     while(prices):
#         price = prices.pop(0)
#         time = 0;
#         for i in range(len(prices)):
#             next_price = prices[i]
#             time += 1
#             if price > next_price:
#                 break
#         answer.append(time)
#     return answer




#효율성 0
# def solution(prices):
#     answer = []
#     down_idxs = []
#
#     for i in range(len(prices)):
#         for j in range(len(prices)):
#             if j in down_idxs:
#                 continue
#             if i == j:
#                 answer.append(0)
#                 break
#
#             if prices[j] > prices[i]:
#                 down_idxs.append(j)
#             answer[j] += 1
#
#     return answer