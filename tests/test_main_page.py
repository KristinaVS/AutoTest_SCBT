from selenium import webdriver

from pages.main_page import MainPage
from pages.picture_page import PicturePage
from pages.search_page import SearchPage

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
link = "https://www.google.com/"


def test_search_enter():
    """ Сценарий 1. Поиск по Enter. """
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.max_window()
    main_page.should_be_search_field_present()
    main_page.add_data("совкомбанк")
    main_page.should_be_table_result_search_present()
    main_page.should_be_result_search("совкомбанк")
    main_page.enter_click()
    search_page = SearchPage(browser, link)
    search_page.should_be_main_result_search_present()
    search_page.should_be_table_result_search_present()
    search_page.should_be_link_main_result_search("sovcombank.ru")
    search_page.should_be_link_table_result_search("sovcombank.ru")


def test_search_button():
    """ Сценарий 1. Поиск по кнопке. """
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.max_window()
    main_page.should_be_search_field_present()
    main_page.add_data("совкомбанк")
    main_page.should_be_table_result_search_present()
    main_page.should_be_result_search("совкомбанк")
    main_page.click_search_button()
    search_page = SearchPage(browser, link)
    search_page.should_be_main_result_search_present()
    search_page.should_be_table_result_search_present()
    search_page.should_be_link_main_result_search("sovcombank.ru")
    search_page.should_be_link_table_result_search("sovcombank.ru")


def test_pictures():
    """ Сценарий 2. Картинки в Google. """
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.max_window()
    main_page.should_be_search_field_present()
    main_page.add_data("совкомбанк")
    main_page.should_be_table_result_search_present()
    main_page.should_be_result_search("совкомбанк")
    main_page.enter_click()
    search_page = SearchPage(browser, link)
    search_page.should_be_main_result_search_present()
    search_page.should_be_table_result_search_present()
    search_page.should_be_link_main_result_search("sovcombank.ru")
    search_page.should_be_link_table_result_search("sovcombank.ru")
    picture_page = PicturePage(browser, link)
    picture_page.should_be_picture_button_present()
    picture_page.click_picture_button()
    picture_page.open_picture(2)
    first_picture = picture_page.get_link_open_picture()
    picture_page.click_forward_button()
    next_picture = picture_page.get_link_open_picture()
    picture_page.should_be_picture_change(first_picture, next_picture)
    picture_page.click_back_button()
    previous_picture = picture_page.get_link_open_picture()
    picture_page.should_be_picture_match(first_picture, previous_picture)
