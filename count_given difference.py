def count_g_diff(n,nums,d):
    s = sum(nums)
    t= (s+S)//2
    n = len(nums)
        
        
    if S > s:
        return 0
    elif (s+S)%2 != 0:
        return 0
    
         
    dp = [[0 for i in range(t +1 )] for j in range(n+1)]
        
        
    for X in range(n+1):
        dp[X][0] = 2**(nums.count(0))
            
          
    for i in range(1,n+1):
        for j in range(1,t +1):
                
            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]
                    
            if nums[i-1] > j or nums[i-1] ==0:
                dp[i][j] = dp[i-1][j]
                    
    return dp[-1][-1]
                
                
    
                
        
    


n = 5
nums = [1,1,1,1,1]
d = 3

print(count_g_diff(n,nums,d))
    