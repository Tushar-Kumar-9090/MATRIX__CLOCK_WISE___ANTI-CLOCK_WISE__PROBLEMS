
#% Problem-1
##  1 2 3 
##  4 5 6 
##  7 8 9

l=[[1,2,3],[4,5,6],[7,8,9]]
n=3
for i in range(n):
    for j in range(n):
        print(l[i][j],end=' ')
    print()





#% Problem-2
#! 90 deg clock-wise
##  7 4 1       
##  8 5 2 
##  9 6 3 

l=[[1,2,3],[4,5,6],[7,8,9]]
n=3
for i in range(n):
    for j in range(n):
        print(l[n-(j+1)][i],end=' ')
    print()






#% Problem-3
#! 90 deg anticlock-wise
##  3 6 9 
##  2 5 8
##  1 4 7

l=[[1,2,3],[4,5,6],[7,8,9]]
n=3
for i in range(n):
    for j in range(n):
        print(l[j][n-(i+1)],end=' ')
    print()






#% Problem-4
##  1 4 7 
##  2 5 8 
##  3 6 9 

l=[[1,2,3],[4,5,6],[7,8,9]]
n=3
for i in range(n):
    for j in range(n):
        print(l[j] [i],end=' ')
    print()







#% Problem-5
##  7 8 9 
##  4 5 6 
##  1 2 3 


l=[[1,2,3],[4,5,6],[7,8,9]]
n=3
for i in range(n):
    for j in range(n):
        print(l[n-(i+1)][j],end=' ')
    print()








#% Problem-6
##  3 2 1 
##  6 5 4 
##  9 8 7

l=[[1,2,3],[4,5,6],[7,8,9]]
n=3
for i in range(n):
    for j in range(n):
        print(l[i][n-(j+1)],end=' ')
    print()







# #% Problem-7
##  9 6 3 
##  8 5 2 
##  7 4 1

l=[[1,2,3],[4,5,6],[7,8,9]]
n=3
for i in range(n):
    for j in range(n):
        print(l[n-(j+1)][n-(i+1)],end=' ')
    print()