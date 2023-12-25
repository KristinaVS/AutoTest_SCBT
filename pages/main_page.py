from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from base.base_class import Base
from base.locators import MainPageLocators


class MainPage(Base):
    # Проверка наличия поля поиска
    def should_be_search_field_present(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD), "Поле поиска не найдено!"

    # Заполнение поля поиска
    def add_data(self, name):
        element = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        element.clear()
        element.send_keys(name)

    # Проверка наличия таблицы с результатами поиска
    def should_be_table_result_search_present(self):
        assert self.is_element_present(*MainPageLocators.TABLE_RESULT_SEARCH), \
            "Таблицы с результатами поиска не найдено!"

    # Проверка результатов поиска
    def should_be_result_search(self, value):
        result_search = self.browser.find_elements(*MainPageLocators.STR_TABLE_RESULT_SEARCH)
        for result in range(len(result_search)):
            text_result = self.browser.find_element(By.XPATH, '//*[@id="Alh6id"]/div[1]/div/ul/li[' + str(result + 1) +
                                                    ']/div/div[2]/div[1]')
            assert value in text_result.text.lower(), "В результате поиска отсутствует искомое слово!"

    # Поиск нажатием на Enter
    def enter_click(self):
        element = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        element.send_keys(Keys.RETURN)

    # Поиск по кнопке
    def click_search_button(self):
        element = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()
