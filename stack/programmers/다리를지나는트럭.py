# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3
# 다리를 지나는 트럭
# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
#
# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.


def update_all_ongoing_trucks_time(ongoing_trucks_times):
    for idx in range(len(ongoing_trucks_times)):
        ongoing_trucks_times[idx] = ongoing_trucks_times[idx] + 1
    return ongoing_trucks_times


def solution(bridge_length, weight, wating_trucks):
    total_time = 0
    ongoing_trucks_weighs = []
    ongoing_trucks_times = []
    passed_trucks = []

    while len(wating_trucks) > 0 or len(ongoing_trucks_weighs) > 0:
        if len(ongoing_trucks_times) == 0:
            ongoing_trucks_weighs.append(wating_trucks.pop(0))
            ongoing_trucks_times.append(0)

        if ongoing_trucks_times[0] >= bridge_length:
            passed_trucks.append(ongoing_trucks_weighs.pop(0))
            ongoing_trucks_times.pop(0)

        if wating_trucks:
            next_truck = wating_trucks[0]
            if avail_on_going(bridge_length, weight, ongoing_trucks_weighs, next_truck):
                ongoing_trucks_weighs.append(wating_trucks.pop(0))
                ongoing_trucks_times.append(0)

        ongoing_trucks_times = update_all_ongoing_trucks_time(ongoing_trucks_times)
        total_time += 1
    return total_time


def avail_on_going(bridge_length, weight, ongoing_trucks_weighs, next_truck):
    # 무게 가능
    weight_avail = sum(ongoing_trucks_weighs) + next_truck <= weight

    # 대수 가능
    count_avail = len(ongoing_trucks_weighs) + 1 <= bridge_length

    return weight_avail & count_avail
