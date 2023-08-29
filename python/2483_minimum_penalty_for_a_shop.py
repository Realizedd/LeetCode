class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        cnt = 0

        for i in range(n):
            if customers[i] == 'Y':
                cnt += 1

        cur_sum = 0
        hour, penalty = 0, float('inf')

        for j in range(0, n + 1):
            if j > 0 and customers[j - 1] == 'Y':
                cur_sum += 1

            customerAfterClose = cnt - cur_sum
            noCustomerBeforeClose = j - cur_sum
            totalPenalty = noCustomerBeforeClose + customerAfterClose

            if totalPenalty < penalty:
                hour = j
                penalty = totalPenalty

        return hour
