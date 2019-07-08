"""
pytest hooks
"""


from common.test_requests import url_list_suite_1, url_list_suite_2, url_list_suite_3


def pytest_addoption(parser):
    """
    addoption - test url
    """
    parser.addoption("--test_url", action="store", default=None,
                     help="my option: 1, 2, 3 or any")


def pytest_generate_tests(metafunc):
    """
    hook for parametrize
    """
    if 'url_list' in metafunc.fixturenames:
        if metafunc.config.getoption('test_url') == '1':
            end = url_list_suite_1()

        elif metafunc.config.getoption('test_url') == '2':
            end = url_list_suite_2()

        elif metafunc.config.getoption('test_url') == '3':
            end = url_list_suite_3()

        elif metafunc.config.getoption('test_url') == 'any':
            end = (url_list_suite_1() + url_list_suite_2() + url_list_suite_3())

        else:
            raise AssertionError('bad test_url, my option: 1, 2, 3 or any')

        metafunc.parametrize("url_list", end)
