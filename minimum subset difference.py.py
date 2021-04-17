def Min_sub_diff(n,arr):
    
    t = sum(arr)
    s=t//2
    
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(s+1):
            if i ==0 :
                dp[i][j] = False
                
            if j ==0:
                
                dp[i][j] = True
                
    
    ans = float('inf')
    
    for i in range(1,n+1):
        for j in range(1,s+1):
            
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                    
            else:
                dp[i][j] = dp[i-1][j]
                
                
    for i in range(0,s+1):
        
        if dp[n][i] == True:
            ans = min(ans,(t - 2*i))
            
    return ans
    
n = 5
arr = [1,6,11,8,20]
print(Min_sub_diff(n,arr))
        
                
                