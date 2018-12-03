"""
    https://www.hackerrank.com/challenges/fraudulent-activity-notifications


"""

import heapq

leftq = [10, 9, 11, 8, 12, 7, 13, 6]

# heapq.heapify(leftq)
heapq._heapify_max(leftq)
while leftq:
    print(heapq._heappop_max(leftq))
# print(leftq)
