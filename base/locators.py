from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.XPATH, '//*[@id="APjFqb"]')
    TABLE_RESULT_SEARCH = (By.XPATH, '//div[@id="Alh6id"]//ul')
    STR_TABLE_RESULT_SEARCH = (By.XPATH, '//*[@id="Alh6id"]//ul/li')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="lJ9FBc"]//input[@class="gNO89b"]')


class SearchPageLocators:
    FIRST_MAIN_RESULT_SEARCH = (By.XPATH, '//div[@id="rso"]//div[@class="eKjLze"]')
    TABLE_MAIN_RESULT_SEARCH = (By.XPATH, '//div[@id="rso"]//div[@class="BYM4Nd"]//table')
    LINK_MAIN_RESULT = (By.XPATH, '//div[@id="rso"]//div[@class="eKjLze"]//span/a')
    STR_TABLE_RESULT = (By.XPATH, '//div[@id="rso"]//div[@class="BYM4Nd"]//table/tbody/tr')


class PicturePageLocators:
    PICTURE_BUTTON = (By.XPATH, '//div[@id="hdtb-msb"]//div[@class="MUFPAc"]//a[text()="Картинки"]')
    ALL_PICTURES = (By.XPATH, '//div[@id="islrg"]/div[1]')
    OPEN_PICTURE = (By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div['
                              '1]/a/img[2]')
    FORWARD_BUTTON = (By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[1]/div/div['
                                '2]/button[2]/div')
    BACK_BUTTON = (By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[1]/div/div['
                             '2]/button[1]/div')
