import heapq
from collections import defaultdict
from math import sqrt

def anomaly_scores(arr, window_size):
    if window_size <= 0 or len(arr) <= window_size:
        return []

    left_heap = []    
    right_heap = []   
    to_remove = defaultdict(int)

    def clean(heap):
        while heap:
            val = -heap[0] if heap is left_heap else heap[0]
            if to_remove[val] > 0:
                heapq.heappop(heap)
                to_remove[val] -= 1
            else:
                break

    def balance():
        if len(left_heap) > len(right_heap) + 1:
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
        elif len(right_heap) > len(left_heap):
            heapq.heappush(left_heap, -heapq.heappop(right_heap))

    def current_median():
        if window_size % 2 == 1:
            return -left_heap[0]
        return (-left_heap[0] + right_heap[0]) / 2

    for i in range(window_size):
        if not left_heap or arr[i] <= -left_heap[0]:
            heapq.heappush(left_heap, -arr[i])
        else:
            heapq.heappush(right_heap, arr[i])
        balance()

    scores = []

    for idx in range(window_size, len(arr)):
        med = current_median()
        scores.append(abs(arr[idx] - med))

        outgoing = arr[idx - window_size]
        incoming = arr[idx]
        to_remove[outgoing] += 1

        if outgoing <= -left_heap[0]:
            clean(left_heap)
        else:
            clean(right_heap)

        if not left_heap or incoming <= -left_heap[0]:
            heapq.heappush(left_heap, -incoming)
        else:
            heapq.heappush(right_heap, incoming)

        balance()
        clean(left_heap)
        clean(right_heap)

    return scores


# -----------------------------------
# Question 2
# -----------------------------------

def top_k_correlated_pairs(dataset, top_k):
    if not dataset or top_k <= 0:
        return []

    row_count = len(dataset)
    col_count = len(dataset[0])

    means = [0.0] * col_count
    stds = [0.0] * col_count

    for col in range(col_count):
        for row in range(row_count):
            means[col] += dataset[row][col]
        means[col] /= row_count

    for col in range(col_count):
        variance = 0.0
        for row in range(row_count):
            diff = dataset[row][col] - means[col]
            variance += diff * diff
        stds[col] = sqrt(variance)

    min_heap = []

    for i in range(col_count):
        for j in range(i + 1, col_count):
            cov = 0.0
            for r in range(row_count):
                cov += (dataset[r][i] - means[i]) * (dataset[r][j] - means[j])

            if stds[i] == 0 or stds[j] == 0:
                corr = 0.0
            else:
                corr = cov / (stds[i] * stds[j])

            abs_corr = abs(corr)

            if len(min_heap) < top_k:
                heapq.heappush(min_heap, (abs_corr, i, j, corr))
            else:
                if abs_corr > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (abs_corr, i, j, corr))

    result = []
    while min_heap:
        _, a, b, c = heapq.heappop(min_heap)
        result.append((a, b, round(c, 4)))

    result.reverse()
    return result

