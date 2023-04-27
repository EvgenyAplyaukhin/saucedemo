import pytest
import allure

case_1 = ['', 'secret_sauce', 'Epic sadface: Username is required']
case_2 = ['zhenya', 'secret_sauce', 'Epic sadface: Username and password do not match any user in this service']
case_3 = ['standard_user', 'qwerty', 'Epic sadface: Username and password do not match any user in this service']
case_4 = ['locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.']


@allure.description('Main page')
@allure.label('owner', 'Jenya')
@allure.title('Successful login')
@allure.suite('Success login')
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(index_page):
    index_page.enter_username()
    index_page.enter_password(password='secret_sauce')
    index_page.click_to_login_btn()
    index_page.check_title()


@allure.description('Error message')
@allure.label('owner', 'Jenya')
@allure.title('Invalid data')
@allure.suite('Unsuccessful_login')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('username, password, expected_result', (case_1, case_2, case_3, case_4))
def test_unsuccessful_login(index_page, username, password, expected_result):
    index_page.enter_wrong_username(username)
    index_page.enter_password(password)
    index_page.click_to_login_btn()
    index_page.check_error_message_container(expected_result)


@allure.description('Authorization')
@allure.label('owner', 'Jenya')
@allure.title('Successful login')
@allure.suite('Logout login')
@allure.severity(allure.severity_level.NORMAL)
def test_logout_login(index_page):
    index_page.enter_username()
    index_page.enter_password(password='secret_sauce')
    index_page.click_to_login_btn()
    index_page.click_to_bm_burger_button()
    index_page.click_to_logout_sidebar_link()


@allure.description('Place an order')
@allure.label('owner', 'Jenya')
@allure.title('By products')
@allure.suite('Сheckout overview')
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_overview(index_page):
    index_page.enter_username()
    index_page.enter_password(password='secret_sauce')
    index_page.click_to_login_btn()
    index_page.click_to_add_to_card()
    index_page.click_to_shopping_cart_link()
    index_page.click_to_checkout()
    index_page.enter_first_name()
    index_page.enter_last_name()
    index_page.enter_zip_postal_cod()
    index_page.click_to_continue()
    index_page.click_to_finish()