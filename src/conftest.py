import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import Locators
import src.utils as utils


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def register_user(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(utils.BASE_URL)
    wait.until(ec.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
    wait.until(ec.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

    email, password = utils.generate_credentials()

    wait.until(ec.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.CONFIRM_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

    return email, password


@pytest.fixture
def login_user(driver, register_user):
    wait = WebDriverWait(driver, 10)

    driver.get(utils.BASE_URL)
    wait.until(ec.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()

    email, password = register_user

    wait.until(ec.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    return email, password
