def req(arr,s):
    n  =len(arr)
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                dp[i][j]  = False
            if j==0:
                dp[i][j]= True
              
            
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1] <= j:
                dp[i][j] = (dp[i-1][j -arr[i-1]] or dp[i-1][j])
            else:
                dp[i][j] =  dp[i-1][j]
                
                
    
        
    
    return dp[n][s]

arr = [1,4,2,5,7,9]
s =20
print(req(arr,s))
