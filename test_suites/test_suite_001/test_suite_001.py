import pytest
import logging as log
#TODO: log.basicConfig(filename="test_suite_001_log.log", level=log.INFO, filemode="w")
http_request_name = 'https://dog.ceo/api' # TODO: Потом в файл-параметры и/или параметр консольного вызова
http_request_name2 = 'https://api.cdnjs.com/'

class TestSuite_001:

    def test_case_001_test_request_dog(self):
        log.debug("Running TestSuite_001, test_case_001, test_request_dog")
        from test_suites.test_suite_001.test_cases.test_case_001 \
            import TestCase_001_test_request as TestCase_001
        request_string = http_request_name + '/breed/hound/images'
        TestCase_001.test_run(self, request_string)

    def test_case_002_test_request_cdnjs(self):
        log.debug("Running TestSuite_002, test_case_002, test_request_cdnjs")
        from test_suites.test_suite_001.test_cases.test_case_002 \
            import TestCase_002_test_request as TestCase_002
        request_string = http_request_name2 + 'libraries'
        request_params = {'output': 'human'}
        TestCase_002.test_run(self, request_string, request_params)
