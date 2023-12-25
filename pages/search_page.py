from selenium.webdriver.common.by import By

from base.base_class import Base
from base.locators import SearchPageLocators


class SearchPage(Base):
    # Проверка главного результата поиска
    def should_be_main_result_search_present(self):
        assert self.is_element_present(*SearchPageLocators.FIRST_MAIN_RESULT_SEARCH), \
            "Главного результата поиска не найдено!"

    # Проверка таблицы с результатами поиска
    def should_be_table_result_search_present(self):
        assert self.is_element_present(*SearchPageLocators.TABLE_MAIN_RESULT_SEARCH), \
            "Таблицы с результатами поиска не найдено!"

    # Проверка результатов поиска по ссылке
    def should_be_link_main_result_search(self, value):
        link_element = self.browser.find_element(*SearchPageLocators.LINK_MAIN_RESULT)
        link_value = link_element.get_attribute('href')
        assert value in link_value, "В ссылке отсуствует искомая часть!"

    # Проверка результатов поиска по ссылке
    def should_be_link_table_result_search(self, value):
        result_search = self.browser.find_elements(*SearchPageLocators.STR_TABLE_RESULT)
        for result in range(len(result_search) - 1):
            element_result = self.browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/table/tbody/tr[' +
                                                       str(result + 1) + ']/td/div/div/div/div/h3/a')
            link_value = element_result.get_attribute('href')
            assert value in link_value, "В ссылке отсуствует искомая часть!"
