# cook your dish here
def equal(arr,Sum):
    n = len(arr)
    
    dp  = [[0 for i in range(Sum//2 +1)] for j in range(n+1)]
    
    
    if Sum%2 != 0:
        return False
    
    for i in range(n+1):
        for j in range(Sum//2 +1 ):
            if i==0:
                dp[i][j] = False
            if j==0:
                dp[i][j] = True
            
        
    for i in range(1,n+1):
        for j in range(1,Sum//2 +1 ):
                
            if arr[i-1]<= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                    
            else:
                dp[i-1][j]
                
                
    return dp[n][Sum//2]
                    
                


Sum = 22
arr = [1,5,11,5,6]
print(equal(arr,Sum))