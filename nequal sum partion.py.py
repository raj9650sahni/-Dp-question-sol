def Nsubsets(n,s,arr):
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(s+1):
            
                
            if i==0:
                dp[i][j] = 0
                
            if j==0:
                dp[i][j] = 1
            
                
                
                
                
    for i in range(1,n+1):
        for j in range(s+1):
            
            if arr[i-1] <=j:
                dp[i][j] = dp[i-1][j- arr[i-1]] + dp[i-1][j]
                
            else:
                
                dp[i][j] = dp[i-1][j]
                
    return dp[-1][-1]
    
    
    
        
   
    
    
n = 7
s = 10
arr = [1,2,4,6,8,5,7]
print(Nsubsets(n,s,arr))