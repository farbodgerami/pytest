import pytest
def test_our_first_test() -> None:
    assert 1==1


# test must be skipped:
@pytest.mark.skip
def test_should_be_skipped() -> None:
  assert 1==2

