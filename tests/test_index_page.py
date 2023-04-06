def test_successful(index_page):
    index_page.enter_username()
    index_page.enter_password()
    index_page.click_to_login_btn()
    index_page.check_title()

def test_unsuccessful(index_page):
    index_page.enter_wrong_username()
    index_page.enter_password()
    index_page.click_to_login_btn()
    index_page.check_error_message_container()
