from companies.models import Company
from unittest import TestCase
from django.test import Client
from django.urls import reverse
import json
import pytest


# @pytest.mark.django_db
# class TestGetCompanies(TestCase):
#     def test_zero_companies_sould_return_empty_list(self) -> None:
#         client = Client()
#         # not a good idea
#         # companies_url = "http://127.0.0.1:8000/companies/"
#         # better:(refer to SimpleRouter)
#         companies_url = reverse("companies:index")

#         response = client.get(companies_url)
#         print(response)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(json.loads(response.content), [])

#     def test_one_company_exists_should_succeed(self) -> None:
#         client = Client()
#         testcompany=Company.objects.create(name="Amazon")
#         companies_url = reverse("companies:index")
#         response = client.get(companies_url)
#         # to see printed result: pytest . -v -s
#         print(response)
#         response_content=json.loads(response.content)[0]

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response_content.get("name"),testcompany.name)
#         self.assertEqual(response_content.get("status"),"Hiring")
#         self.assertEqual(response_content.get("application_link"),"")
#         testcompany.delete()


# @pytest.mark.django_db
# class TestGetCompanies(TestCase):
#     # client = Client()
#     def setUp(self) -> None:
#         self.client = Client()
#         self.companies_url = reverse("companies:index")

#     # this function runs everytime our test is running:
#     def tearDown(self) -> None:
#         pass

#     def test_zero_companies_sould_return_empty_list(self) -> None:
#         response = self.client.get(self.companies_url)
#         print(response)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(json.loads(response.content), [])

#     def test_one_company_exists_should_succeed(self) -> None:
#         testcompany = Company.objects.create(name="Amazon")
#         response = self.client.get(self.companies_url)

#         response_content = json.loads(response.content)[0]
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response_content.get("name"), testcompany.name)
#         self.assertEqual(response_content.get("status"), "Hiring")
#         self.assertEqual(response_content.get("application_link"), "")
#         testcompany.delete()


@pytest.mark.django_db
class BasicCompanyApiTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies:index")

    # this function runs everytime our test is running:
    def tearDown(self) -> None:
        pass


class TestGetCompanies(BasicCompanyApiTestCase):

    def test_zero_companies_sould_return_empty_list(self) -> None:
        response = self.client.get(self.companies_url)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_succeed(self) -> None:
        testcompany = Company.objects.create(name="Amazon")
        response = self.client.get(self.companies_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), testcompany.name)
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        testcompany.delete()


class TestPostCompanies(BasicCompanyApiTestCase):
    def test_create_company_without_arguments_sould_fall(self) -> None:
        # first test it with postman and then get the output here("This field is required.")
        response = self.client.post(path=self.companies_url)
        response = self.client.post(path=self.companies_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content), {"name": ["This field is required."]}
        )

    def test_create_existing_company_should_fail(self) -> None:
        Company.objects.create(name="amazon")
        response = self.client.post(path=self.companies_url, data={"name": "amazon"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content),
            {"name": ["company with this name already exists."]},
        )

    def test_create_company_with_only_name_all_fields_should_be_default(self) -> None:
        response = self.client.post(
            path=self.companies_url, data={"name": "test company name"}
        )
        response_content = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")

    def test_create_company_with_layoffs_status_should_succeed(self) -> None:
        response = self.client.post(
            path=self.companies_url,
            data={"name": "test company name", "status": "Layoffs"},
        )
        response_content = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_content.get("status"), "Layoffs")

    def test_create_company_with_wront_status_should_fail(self) -> None:
        response = self.client.post(
            path=self.companies_url,
            data={"name": "test company name", "status": "wrongstatus"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("wrongstatus", str(response.content))
        self.assertIn("is not a valid choice.", str(response.content))

    # xfail:its oke of this test fail
    @pytest.mark.xfail
    def test_should_be_ok_if_fails(self) -> None:
        self.assertEqual(1, 2)


def raise_covid19_exception() -> None:
    raise ValueError("corona viruse exception")


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "corona viruse exception" == str(e.value)


# caplog fixture,assert logs
import logging

logger = logging.getLogger("CORONA_LOGS")


def function_that_logs_something() -> None:
    try:
        raise ValueError("CoronaVirus Exception")
    except ValueError as e:
        logger.warning(f"i am logging {str(e)}")


def test_logged_warning_level(caplog) -> None:
    function_that_logs_something()
    assert "i am logging CoronaVirus Exception" in caplog.text


# work on 23
# logger=logging.getLogger('CORONA_LOGS')

# def test_logged_warning_level(caplog)-> None:
#     logger.warning(f"1111")
#     print(caplog.text)
#     assert '1111' in caplog.text
