import pytest

def test_our_first_test() -> None:
    assert 1 == 1


# test must be skipped:
@pytest.mark.skip
def test_should_be_skipped() -> None:
  assert 1 == 2

@pytest.mark.skipif(4 >1,reason="skipped becouse 4>1")
def test_should_be_skipped_if()-> None:
    assert 1 == 2
    
# teset we are oke with them of failing
@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1==2
    
@pytest.mark.slow
def test_slow() -> None:
    pass