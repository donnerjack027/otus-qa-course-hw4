"""
test_suite_001
"""
from test_suites.test_suite_001.test_cases.cases import TestCases


class TestSuite1:
    """
    Class test suite
    """

    @staticmethod
    def test_status_code_run(url_list):
        """
        test_status_code_run
        """
        TestCases.status_response_check(url_list)

    @staticmethod
    def test_status_run(url_list):
        """
        test_status_run
        """
        TestCases.status_json_response_check(url_list)

    @staticmethod
    def test_header_run(url_list):
        """
        test_header_run
        """
        TestCases.headers_response_check(url_list)
