from companies.models import Company
from unittest import TestCase
from django.test import Client
from django.urls import reverse
import json
import pytest


# instead of @pytest.mark.django_db  on any of function add this here:
pytestmark =pytest.mark.django_db
companies_url = reverse("companies:index")
 

 
# client is a predifined fixture in pytes-django
def test_zero_companies_sould_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code== 200
    assert json.loads(response.content)== []
    
 
def test_one_company_exists_should_succeed(client) -> None:
    testcompany = Company.objects.create(name="Amazon")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code== 200
    assert response_content.get("name")== testcompany.name
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",json.loads(response.content))
    assert response_content.get("status")== "Hiring"
    assert response_content.get("application_link")== ""
    # becouse every test is isolated so remove bellow
    # testcompany.delete()


 
def test_create_company_without_arguments_sould_fall(client) -> None:
    # first test it with postman and then get the output here("This field is required.")
    response = client.post(path=companies_url)
    response = client.post(path=companies_url)
    assert response.status_code== 400
    assert json.loads(response.content) == {"name": ["This field is required."]}
    

 
def test_create_existing_company_should_fail(client) -> None:
    Company.objects.create(name="amazon")
    response = client.post(path=companies_url, data={"name": "amazon"})
    assert response.status_code== 400
    assert json.loads(response.content)=={"name": ["company with this name already exists."]}
    

 
def test_create_company_with_only_name_all_fields_should_be_default(client) -> None:
    response = client.post(
        path=companies_url, data={"name": "test company name"}
    )
    response_content = json.loads(response.content)
    assert response.status_code==201
    assert response_content.get("status")=="Hiring"
    assert response_content.get("application_link") == ""

 
def test_create_company_with_layoffs_status_should_succeed(client) -> None:
    response = client.post(
        path=companies_url,
        data={"name": "test company name", "status": "Layoffs"},
    )
    response_content = json.loads(response.content)
    assert response.status_code== 201
    assert response_content.get("status")== "Layoffs"

 
def test_create_company_with_wront_status_should_fail(client) -> None:
    response = client.post(
        path=companies_url,
        data={"name": "test company name", "status": "wrongstatus"},
    )
    assert response.status_code== 400
    assert "wrongstatus" in str(response.content)
    assert "is not a valid choice." in str(response.content)

# xfail:its oke of this test fail
@pytest.mark.xfail
def test_should_be_ok_if_fails( ) -> None:
   assert 1 == 2
@pytest.mark.skip
def test_should_be_skipped()->None:
    assert 1==2

# def raise_covid19_exception() -> None:
#     raise ValueError("corona viruse exception")


# def test_raise_covid19_exception_should_pass() -> None:
#     with pytest.raises(ValueError) as e:
#         raise_covid19_exception()
#     assert "corona viruse exception" == str(e.value)


# # caplog fixture,assert logs
# import logging

# logger = logging.getLogger("CORONA_LOGS")


# def function_that_logs_something() -> None:
#     try:
#         raise ValueError("CoronaVirus Exception")
#     except ValueError as e:
#         logger.warning(f"i am logging {str(e)}")


# def test_logged_warning_level(caplog) -> None:
#     function_that_logs_something()
#     assert "i am logging CoronaVirus Exception" in caplog.text


# work on 23
# logger=logging.getLogger('CORONA_LOGS')

# def test_logged_warning_level(caplog)-> None:
#     logger.warning(f"1111")
#     print(caplog.text)
#     assert '1111' in caplog.text
