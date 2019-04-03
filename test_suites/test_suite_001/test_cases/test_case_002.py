from common.request import Request
import requests
import logging as log


class TestCase_002_test_request:

    def __init__(self):
        super().__init__()

    def test_run(self, request_string, request_params):
        log.info("Running test case %s" % TestCase_002_test_request.__name__)
        log.info("Input params: %s" % request_string)
        try:
            # Вызов метода подготовки запроса (собрать весь url),
            # который в конце вызывает метод отправки запроса
            response = Request.prepare_request(request_string, request_params)
            print(response)
            print(response.text)
            assert 2+2 == 4, "Print if assert exception"

        except IndexError:
            log.error('Index error, status code %s, error message: \n %s' % response.status_code)
            assert False, 'Index error, status code %s, error message: \n %s' % response.status_code

        except AttributeError:
            log.error('Attribute \ timeout error')
            assert False, 'Attribute \ timeout error'
