from testpage import OperationHelper
import logging


def test_step1(browsser):
    logging.info("Test 1 Starting")
    testpage = OperationHelper(browsser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

