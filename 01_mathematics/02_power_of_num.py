"""
Given two integers x and n, write a function to compute xn.
We may assume that x and n are small and overflow doesn’t happen.

Time Complexity: O(log n)
Auxiliary Space: O(log n),
Reg: https://www.geeksforgeeks.org/batch/dsa-python-self-paced-april/track/mathematics-basics-python/article/NjEzMA%3D%3D

"""

'''since the loop is running for n times
   time complexity : O(n)
   space Complexity: O(n)
   
   when input grows execution time increases.e.g.,2* 3245689 it's almost 5 min 
'''


def power1(base, p):
    power = 1
    for i in range(p):
        power = power * base
    return power

base = int(input(f"enter base"))
power = int(input(f"enter power"))
product = power1(base, power)
print(product)

'''
optimization is required, use recursion + divide conquer algs to have optimzed code 
'''
