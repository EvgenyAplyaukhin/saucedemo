import allure

@allure.description('Place an order')
@allure.label('owner', 'Jenya')
@allure.title('By products')
@allure.suite('Сheckout overview')
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_overview(main_page, index_page):
    index_page.enter_username()
    index_page.enter_password(password='secret_sauce')
    index_page.click_to_login_btn()
    main_page.click_to_add_to_card()
    main_page.click_to_shopping_cart_link()
    main_page.click_to_checkout()
    main_page.enter_first_name()
    main_page.enter_last_name()
    main_page.enter_zip_postal_cod()
    main_page.click_to_continue()
    main_page.click_to_finish()