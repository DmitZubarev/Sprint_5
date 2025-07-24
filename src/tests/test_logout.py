from pytest_check import check
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import Locators


class TestLogout:

    # Проверка деавторизации
    def test_logout(self, driver, login_user):
        wait = WebDriverWait(driver, 10)

        wait.until(ec.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()

        login_button = wait.until(ec.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON))
        user_avatar = driver.find_elements(*Locators.USER_AVATAR)
        user_name = driver.find_elements(*Locators.USER_NAME)

        # проверяем, что аватар и кнопка больше не отображаются
        with check:
            assert len(user_avatar and user_name) == 0, "Аватар и кнопка выхода отображаются после деавторизации"

        # проверяем, что появилась кнопка "Вход и регистрация"
        with check:
            assert login_button.is_displayed(), 'Отсутствует кнопка "Вход и регистрация"'
