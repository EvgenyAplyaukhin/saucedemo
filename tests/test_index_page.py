import pytest

case_1 = ['', 'secret_sauce', 'Epic sadface: Username is required']
case_2 = ['zhenya', 'secret_sauce', 'Epic sadface: Username and password do not match any user in this service']
case_3 = ['standard_user', 'qwerty', 'Epic sadface: Username and password do not match any user in this service']
case_4 = ['locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out']


def test_successful_login(index_page):
    index_page.enter_username()
    index_page.enter_password(password='secret_sauce')
    index_page.click_to_login_btn()
    index_page.check_title()

@pytest.mark.parametrize('username, password, expected_result', (case_1, case_2, case_3,case_4))
def test_unsuccessful_login(index_page, username, password, expected_result):
    index_page.enter_wrong_username(username)
    index_page.enter_password(password)
    index_page.click_to_login_btn()
    index_page.check_error_message_container(expected_result)


def test_logout(index_page):
    index_page.enter_username()
    index_page.enter_password()
    index_page.click_to_login_btn()
    index_page.click_to_bm_burger_button()
    index_page.click_to_logout_sidebar_link()
