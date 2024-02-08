# Le tableau de matrice :
# x*y | 1 2 3 4 5 6 7 8 9 10
# --------------------------
# 1   | 1 2 3 4 5 6 7 8 9 10
# 2   | 2 4 ...
# 3   | ....
# 4   |
# 5   |

for i in range (1,11) :
    for j in range (1,11) :
        N = i * j 
        print(i , "x", j , "=", N)




