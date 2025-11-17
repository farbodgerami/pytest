import pytest

# def test_our_first_test() -> None:
#     assert 1 == 1


# # test must be skipped:
# @pytest.mark.skip
# def test_should_be_skipped() -> None:
#   assert 1 == 2

# @pytest.mark.skipif(4 >1,reason="skipped becouse 4>1")
# def test_should_be_skipped_if()-> None:
#     assert 1 == 2
    
# # teset we are oke with them of failing
# @pytest.mark.xfail
# def test_dont_care_if_fails() -> None:
#     assert 1==2
 
# # this must be registered in the pytest.ini file   
# @pytest.mark.slow
# def test_slow() -> None:
#     pass

#usein fixtures befor of after test for example initializing a database
class Company:
    def __init__(self,name:str, stock_symbol: str):
        self.name=name
        self.stock_symbol = stock_symbol
    
    def __str__(self):
        return f"{self.name} : {self.stock_symbol}"


@pytest.fixture
def company() -> Company:
    return Company(name="james",stock_symbol="hetfield")

def test_with_fixture(company:Company) -> None:
    print(f"printing {company} from fixture")


@pytest.mark.parametrize("company_name",["TikTok","Instagram","Twitch"],ids=["tik","inst","twi"])
def test_parametrized(company_name) -> None:
    print(f"\nTest with {company_name}")

def raise_covid19_exception() -> None:
    raise ValueError("Corona Virous exception")

def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "Corona Virous exception" == str(e.value)