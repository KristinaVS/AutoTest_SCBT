from selenium.webdriver.common.by import By

from base.base_class import Base
from base.locators import PicturePageLocators


class PicturePage(Base):
    # Проверка наличия кнопки "Картинки"
    def should_be_picture_button_present(self):
        assert self.is_element_present(*PicturePageLocators.PICTURE_BUTTON), "Кнопка 'Картинки' не найдена!"

    # Нажатие по кнопке "Картинки"
    def click_picture_button(self):
        element = self.browser.find_element(*PicturePageLocators.PICTURE_BUTTON)
        element.click()

    # Открытие картинки и проверка, что открылась выбранная картинка
    def open_picture(self, number):
        start_picture = self.browser.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[' + str(number) +
                                                  ']/a[1]/div[1]/img')
        link_start_picture = start_picture.get_attribute('src')
        start_picture.click()
        assert self.is_element_present(*PicturePageLocators.OPEN_PICTURE), "Картинка не открыта!"
        link_open_picture = self.get_link_open_picture()
        self.should_be_picture_match(link_start_picture, link_open_picture)

    # Нажатие на кнопку 'Вперед'
    def click_forward_button(self):
        element = self.browser.find_element(*PicturePageLocators.FORWARD_BUTTON)
        element.click()

    # Нажатие на кнопку 'Назад'
    def click_back_button(self):
        element = self.browser.find_element(*PicturePageLocators.BACK_BUTTON)
        element.click()

    # Получение ссылки открытой картинки
    def get_link_open_picture(self):
        picture = self.browser.find_element(*PicturePageLocators.OPEN_PICTURE)
        link_picture = picture.get_attribute('src')
        return link_picture

    # Проверка, что картинка изменилась
    def should_be_picture_change(self, first_picture, second_picture):
        assert first_picture != second_picture, 'Картинка не изменилась!'

    # Проверка, что картинки совпадают
    def should_be_picture_match(self, first_picture, second_picture):
        assert first_picture == second_picture, 'Картинки не совпадают!'
