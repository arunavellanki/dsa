# User function Template for python3

class Solution:
    ##Complete the below codes
    # Function to find median of the array elements.
    def median(self, A, N):
        A.sort()
        # print(A)
        if N % 2 == 0:
            idx = N // 2
            # print(idx)
            median = (A[idx] + A[idx - 1]) // 2
            return median

        if N % 2 != 0:
            # print(A)
            middle_idx = N // 2
            # print(middle_idx)
            return A[middle_idx]

        ##Your code here
        # If median is fraction then convert the median to integer and return

    # Function to find mean of the array elements.
    def mean(self, A, N):
        mean = sum(A) // N
        return mean
        ##Your code here


A = [2, 4, 19, 20, 3]
N = 5
sol = Solution()
mean = sol.mean(A, N)
median = sol.median(A, N)
print(f"the mean and median of the list are {mean}, {median}")
