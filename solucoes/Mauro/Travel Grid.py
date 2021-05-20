def grid_traveler(m, n, memo = {}):
     
     if m == 1 and n == 1:
          return 1
     
     elif m == 0 or n == 0:
          return 0
     
     elif str(m) + "." + str(n) in memo:
          return memo[str(m) + "." + str(n)]
     

     memo.update({str(m) + "." + str(n) : grid_traveler(m - 1, n) + grid_traveler(m, n - 1)})
     
     
     return memo[str(m) + "." + str(n)]