from pytest_check import check
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import Locators
import src.utils as utils


class TestLogin:

    # Проверка авторизации
    def test_login(self, driver, register_user):
        wait = WebDriverWait(driver, 10)

        driver.get(utils.BASE_URL)
        wait.until(ec.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()

        email, password = register_user

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        user_avatar = wait.until(ec.visibility_of_element_located(Locators.USER_AVATAR))
        user_name = wait.until(ec.visibility_of_element_located(Locators.USER_NAME))

        # проверяем переход на главную
        with check:
            assert utils.BASE_URL == driver.current_url, 'Не произошёл переход на главную страницу'

        # проверяем отображение аватара
        with check:
            assert user_avatar.is_displayed(), 'Аватар пользователя не отображается'

        # проверяем отображение имени
        with check:
            assert user_name.text == 'User.', f'Ожидаемое имя "User.", фактическое "{user_name.text}"'
