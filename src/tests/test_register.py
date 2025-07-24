from pytest_check import check
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import Locators
import src.utils as utils


class TestRegister:

    # Проверка регистрации
    def test_register_success(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get(utils.BASE_URL)
        wait.until(ec.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(ec.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        email, password = utils.generate_credentials()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        user_avatar = wait.until(ec.visibility_of_element_located(Locators.USER_AVATAR))
        user_name = wait.until(ec.visibility_of_element_located(Locators.USER_NAME))

        # проверяем переход на главную
        with check:
            assert utils.BASE_URL == driver.current_url, 'Не произошёл редирект на главную страницу после авторизации'

        # проверяем отображение аватара
        with check:
            assert user_avatar.is_displayed(), 'Аватар пользователя не отображается'

        # проверяем отображение имени
        with check:
            assert user_name.text == 'User.', f'Ожидаемое имя "User.", фактическое "{user_name.text}"'


    # Проверка регистрации c email не по маске *******@*******.***
    def test_register_with_invalid_email_format(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get(utils.BASE_URL)
        wait.until(ec.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(ec.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        email = utils.invalid_email()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_message = wait.until(ec.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))

        # проверяем цвет полей
        with check:
            assert utils.is_error_red(driver.find_element(*Locators.EMAIL_BORDER)), 'Поле "Email" не в ошибке'
        with check:
            assert utils.is_error_red(driver.find_element(*Locators.PASSWORD_BORDER)), 'Поле "Пароль" не в ошибке'
        with (check):
            assert utils.is_error_red(driver.find_element(*Locators.CONFIRM_PASSWORD_BORDER)), 'Поле "Повторите пароль" не в ошибке'

        # проверяем наличие ошибки
        with check:
            assert error_message.is_displayed() and error_message.text == 'Ошибка', 'Сообщение об ошибке отсутствует'


    # Проверка регистрации уже существующего пользователя
    def test_register_(self, driver, register_user):
        wait = WebDriverWait(driver, 10)

        driver.get(utils.BASE_URL)
        wait.until(ec.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(ec.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        email, password = register_user

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_message = wait.until(ec.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))

        # проверяем цвет полей
        with check:
            assert utils.is_error_red(driver.find_element(*Locators.EMAIL_BORDER)), 'Поле "Email" не в ошибке'
        with check:
            assert utils.is_error_red(driver.find_element(*Locators.PASSWORD_BORDER)), 'Поле "Пароль" не в ошибке'
        with (check):
            assert utils.is_error_red(driver.find_element(*Locators.CONFIRM_PASSWORD_BORDER)), 'Поле "Повторите пароль" не в ошибке'

        # проверяем наличие ошибки
        with check:
            assert error_message.is_displayed() and error_message.text == 'Ошибка', 'Сообщение об ошибке отсутствует'
