"""
test cases
"""
import logging
import requests


class TestCases:
    """
    Class test cases
    """
    @staticmethod
    def status_response_check(request):
        """
        status_response_check
        """
        temp = requests.get(str(request))
        r_status = temp.status_code
        logging.debug('Response status code: %s', r_status)
        assert r_status == 200

    @staticmethod
    def status_json_response_check(request):
        """
        status_json_response_check
        """
        temp = requests.get(str(request)).json()
        r_status = temp.get('status')
        logging.debug('Response status: %s', r_status)
        assert r_status == "success"

    @staticmethod
    def headers_response_check(request):
        """
        headers_response_check
        """
        temp = requests.get(str(request))
        r_headers = temp.headers
        logging.debug('Response headers: %s', r_headers)
        assert len(r_headers) > 0
