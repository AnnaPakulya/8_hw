from pages.elemets_page import ElementsPage
import time

# def test_visible_btn_side (browser):
#
#     elements_page = ElementsPage(browser)
#
#     elements_page.visit()
#     elements_page.btn_sidebar_first.click()
#     time.sleep(3)
#     #assert elements_page.btn_sidebar_first_textbook.exist()
#     assert not elements_page.btn_sidebar_first_textbox.visible()

def test_go_to_page_elements (browser):

    elements_page = ElementsPage(browser)

    elements_page.visit()

    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(3)
    #assert elements_page.btn_sidebar_first_textbook.exist()
    assert not elements_page.btn_sidebar_first_checkbox.visible()