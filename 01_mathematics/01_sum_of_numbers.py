"""Given a number n, find the sum of first natural numbers.
   Time Complexity: O(1)
   Auxiliary Space: O(1)



"""


def sum_numbers(n):
    sum = (n * n + 1) / 2
    return sum


num = int(input(f"enter number to find sum"))
sum = sum_numbers(num)
print(f"sum of numbers till {num}, is {sum}")
