first go to the project location otherwise you get error:
cd crtech

pytest .

### more specific:
pytest ./gist/test_gist.py -v

 
### run with a specific mark:
pytest ./gist/test_gist.py -v -p no:warnings -m slow

### exclude a specific mark:
pytest ./gist/test_gist.py -v -p no:warnings -m "not slow"


pytest ./gist/test_gist.py -v -p no:warnings -s

to see printed result: pytest . -v -s

install black and then black .


### to run specific test:
pytest -k test_raise_covid19_exception_should_pass -v -s

 
pytest -v -s --durations=0 /home/farbod/Desktop/dev/inprogress/pytest/crtech/companies/tests/test_api.py

dir:
pytest -v -s --durations=0 /home/farbod/Desktop/dev/inprogress/pytest/crtech/companies/tests/

reletive path

#### all the tests has keyword in it
pytest -k keyword -v -s

test in the keyword and zero is excluded
pytest -k "test and not zero" -v -s

#### specific class
pytest -v -s --durations=0 /home/farbod/Desktop/dev/inprogress/pytest/crtech/companies/tests/test_api.py::TestPostCompanies

#### specific method
pytest -v -s --durations=0 /home/farbod/Desktop/dev/inprogress/pytest/crtech/companies/tests/test_api.py::TestPostCompanies::test_create_existing_company_should_fail

#### specific marker:
pytest -v -s --durations=0 -m xfail