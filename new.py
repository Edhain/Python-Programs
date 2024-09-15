# def grid_paths(n,m):
#     if n==1 or m==1:
#         return 1
#     else:
#         return grid_paths(n-1,m) + grid_paths(n,m-1)
    
# print(grid_paths(3,4))

# def reverse_string(str):
#     if len(str)==1:
#         return str
#     else:
#         return reverse_string(str[1:]) + str[0]

# print(reverse_string('Hello'))

# class Solution:
#     def reverseString(self, s) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         if len(s)==1:
#             return s
#         else:
#             return self.reverseString(s[1:]) + s[0]

# s = ["h","e","l","l","o"]
# print(reverseString(s))

# class mine:
#     def recur(self, num):
#         print(num, end="")
#         if num > 1:
#             print(" * ",end="")
#             return num * self.recur(self, num-1)
#         print(" =")
#         return 1

# def main():
#     a = mine()
#     print(mine.recur(mine, 10))

# main()
u=[1,2,3,4,5]
u.remove(2)
print(u)
import sin from math