pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
pytest -v -s --html=Reports/report.html  testCases/ --browser chrome
pytest -v -s --html=Reports/report.html  testCases/test_searchCustomerByName.py --browser chrome
pytest -v -s --html=Reports/report.html  testCases/test_searchCustomerByEmail.py --browser chrome
pytest -v -s --html=Reports/report.html  testCases/test_addCustomer.py --browser chrome
pytest -v -s -n=2 --html=Reports/report.html  testCases/test_login_ddt.py --browser chrom
