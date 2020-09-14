def test_find_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    try:
        browser.find_element_by_css_selector('[type="submit"].btn-lg')
    except:
        assert False, 'cart button not found'

        