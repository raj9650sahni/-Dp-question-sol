  def Minimum_Coin_count(self, S, m, n): 
        
        dp = [[0 for i in range(n+1)] for j in range(m+1) ]
        
        for i in range(m+1):
            dp[i][0] = 1
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if S[i-1] <= j:
                    dp[i][j] = dp[i][j-S[i-1]] + dp[i-1][j]
                    
                else:
                    
                    dp[i][j] = dp[i-1][j]
                    
        return dp[m][n]