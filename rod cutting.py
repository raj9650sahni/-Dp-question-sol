def rodCutting(n,arr,prices):
    
   
    
    dp = [[0 for i in range(n+1)] for j in range(len(arr)+1)]
    
    for i in range(len(arr)+1):
        for j in range(n+1):
            
            if i==0:
                dp[i][j] = 0
                
            if j==0:
                dp[i][j] = 0
                
                
                
    for i in range(1,len(arr)+1):
        for j in range(1,n+1):
            
            if arr[i-1] <=j:
                dp[i][j] = max(prices[i-1] + dp[i][j-arr[i-1]] ,dp[i-1][j])
            
            else:
                
                dp[i][j] = dp[i-1][j]
                
                
                
    return dp[n][n]
                
                
n =8
arr = [1,2, 3 , 4 ,5 , 6 ,7 , 8 ]
prices = [ 3 ,5, 8 ,9 ,10 ,17,17,20]
print(rodCutting(n,arr,prices))
                
    