from time import sleep

def test_check_btn_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert len(browser.find_elements_by_css_selector('.btn-add-to-basket')) == 1, "There is no button to add to basket"
    sleep(10)