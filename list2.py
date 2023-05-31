

# #% Problem-1
# ## o/p:- 18

# l=[[1,2,3],[4,5,6],[7,8,9]]
# first=0
# middle=0
# last=0
# n=3
# for i in range(n):
#     first+=l[0][i]
#     middle+=l[1][i]
#     last+=l[n-1][i]
# print(first)
# print(middle)
# print(last)
# print(abs(first-last))






# #% Problem-2
# ## o/p:-30

# l=[[1,2,3],[4,5,6],[7,8,9]]
# first=0
# middle=0
# last=0
# n=3
# for i in range(n):
#     first+=l[i][0]
#     middle+=l[i][1]
#     last+=l[i][n-1]

# print(first)
# print(middle)
# print(last)
# print(first+last)







# #% Problem-3
# ## o/p:-30

# l=[[1,2,3],[4,5,6],[7,8,9]]
# first=0
# last=0
# n=3
# for i in range(n):
#     first+=l[n//2][i]
#     last+=l[i][n//2]
# print(first+last)






# #% Problem-4
# ## o/p:-225

# l=[[1,2,3],[4,5,6],[7,8,9]]
# d=0
# ad=0
# n=3
# for i in range(n):
#     d+=l[i][i]
#     ad+=l[i][n-(i+1)]
# print(d*ad)






#% Problem-5

          *
        *   *
      *       *       
    *           *     
  *               *   
*                   * 
  *               *   
    *           *     
      *       *       
        *   *
          *

n=11
for i in range(n):
    for j in range(n):
        if i+j==n//2 or abs(i-j)==n//2 or i+j==3*(n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()