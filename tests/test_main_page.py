import allure

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