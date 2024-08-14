# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.

# Test Cases:
# a=[1,2] b=[1] -> [2]
# a=[1,2,2,2,3] b=[2,3] -> [1]
# a=[18, 8, -14] b=[8, -20, -16, -18] -> [18, -14]
# a=[6, -9, -1] b=[-3, -4, 17, -4, 10, -16, -12, 11, -2, 17, 2, 1, 6] -> [-9, -1]
# a=[-8, -2, -4, 13, 10, -12, -3, 6] b=[-3, 17] -> [-8, -2, -4, 13, 10, -12, 6]


def element(a,b):
    b_set = set(b)
    return [item for item in a if item not in b_set]

print(element([1, 2], [1]))
print(element([1,2,2,2,3], [2,3]))
print(element([18, 8, -14], [8, -20, -16, -18]))
print(element([6, -9, -1],[17, -4, 10, -16, -12, 11, -2, 17, 2, 1, 6]))
print(element([-8, -2, -4, 13, 10, -12, -3, 6],[[-3, 17]]))
