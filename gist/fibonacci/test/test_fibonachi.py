from fibonacci.naive import fibonachi_naive

def test_naive()-> None:
    res=fibonachi_naive(n=0)
    assert res ==0
    
    res=fibonachi_naive(n=1)
    assert res ==1
     
    res=fibonachi_naive(n=20)
    assert res ==6765
    
   
# much better alternative with pytest
import pytest
@pytest.mark.parametrize("n,expected",[(0,0),(1,1),(20,6765)])
def test_naive(n:int,expected:int)-> None:
    res=fibonachi_naive(n=n)
    assert res == expected
    
  