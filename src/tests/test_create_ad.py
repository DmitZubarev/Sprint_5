from pytest_check import check
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import Locators
import src.utils as utils
import random


class TestPostAd:

    # Проверка создания объявления неавторизованным пользователем
    def test_post_ad_unauthorized_user(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get(utils.BASE_URL)
        driver.find_element(*Locators.POST_AD_BUTTON).click()

        expected_title = 'Чтобы разместить объявление, авторизуйтесь'
        modal_title = wait.until(ec.visibility_of_element_located(Locators.MODAL_HEADER)).text

        # проверяем наличие модального окна с искомым заголовком
        with check:
            assert modal_title == expected_title, f'Ожидаемый заголовок "{expected_title}", фактический "{modal_title}"'


    # Проверка создания объявления авторизованным пользователем
    def test_post_ad_authorized_user(self, driver, login_user):
        wait = WebDriverWait(driver, 10)

        wait.until(ec.element_to_be_clickable(Locators.USER_AVATAR))
        driver.find_element(*Locators.POST_AD_BUTTON).click()

        title, description, price = utils.generate_ad_data()

        # заполняем текстовые поля
        driver.find_element(*Locators.TITLE_INPUT).send_keys(title)
        driver.find_element(*Locators.PRODUCT_DESCRIPTION_INPUT).send_keys(description)
        driver.find_element(*Locators.PRICE).send_keys(price)

        # выбираем любую категорию
        random_category = random.choice(Locators.CATEGORY_OPTION)
        driver.find_element(*Locators.CATEGORY_DROPDOWN).click()
        wait.until(ec.visibility_of_element_located(random_category)).click()

        # выбираем любой город
        random_city = random.choice(Locators.CITY_OPTION)
        driver.find_element(*Locators.CITY_DROPDOWN).click()
        wait.until(ec.visibility_of_element_located(random_city)).click()

        # выставляем радио-баттон
        driver.find_element(*Locators.CONDITION_OLD_RADIO).click()

        # публикуем объявление
        driver.find_element(*Locators.PUBLISH_AD_BUTTON).click()
        wait.until(ec.presence_of_element_located(Locators.SEARCH_INPUT))

        # переходим в профиль искать объявление
        driver.find_element(*Locators.USER_AVATAR).click()
        wait.until(ec.visibility_of_element_located(Locators.PAGINATION_BACK_MY_BUTTON))
        my_ad_titles = [el.text for el in driver.find_elements(*Locators.MY_AD_CARDS_TITLE)]

        # проверяем наличие объявления с искомым заголовком
        with check:
            assert title in my_ad_titles, 'Созданное объявление отсутствует в профиле'
