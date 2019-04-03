import requests
import logging as log


class Request:

    @staticmethod
    def send_request(request_string, request_params, timeout):
        try:
            response = requests.get(request_string, params=request_params, timeout=timeout)
            log.debug("Executing request %s" % response.url)
            return response
        except requests.exceptions.ReadTimeout:
            log.error('Read timeout while executing request %s' % request_string)
            return requests.exceptions.ReadTimeout
        except requests.exceptions.ConnectTimeout:
            log.error('Connection timeout occurred while executing request %s' % request_string)
            return requests.exceptions.ConnectTimeout

    @staticmethod
    def prepare_request(request_string, request_params=None, timeout=1):
        """Preparing request string from base url, http request name and passing forward to send"""
        log.debug('Request string is %s' % request_string)
        if request_params:
            log.debug('Request params is %s' % request_params)
        response = Request.send_request(request_string, request_params, timeout)
        return response
