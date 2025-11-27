def fibonachi_naive(n:int)->int:
    if n==0 or n==1:
        return n
    
    return fibonachi_naive(n-2)+fibonachi_naive(n-1)
    