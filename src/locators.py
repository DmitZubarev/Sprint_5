from selenium.webdriver.common.by import By


class Locators:

    # Логотип
    LOGO = (By.CSS_SELECTOR, '//*[contains(@class, "header_logo")]')

    # Кнопка "Вход и регистрация"
    LOGIN_REGISTER_BUTTON = (By.XPATH, '//button[text()="Вход и регистрация"]')

    # Кнопка "Разместить объявление"
    POST_AD_BUTTON = (By.XPATH, '//button[@type="button" and contains(text(), "Разместить объявление")]')

    # Поле поиска "Я хочу купить"
    SEARCH_INPUT = (By.XPATH, '//input[(@name="name") and (@placeholder="Я хочу купить...")]')

    # Кнопка поиска
    SEARCH_BUTTON = (By.XPATH, '//button[contains(@class, "arrowButton--right icon")]')

    # Выпадающий список категорий
    CATEGORY_DROPDOWN = (By.XPATH, '(//button[contains(@class, "dropDownMenu_arrowDown")])[1]')

    # Опция категории
    CATEGORY_OPTION = [
        (By.XPATH, '//button[./span[starts-with(text(), "Авт")]]'),
        (By.XPATH, '//button[./span[starts-with(text(), "Кни")]]'),
        (By.XPATH, '//button[./span[starts-with(text(), "Сад")]]'),
        (By.XPATH, '//button[./span[starts-with(text(), "Хоб")]]'),
        (By.XPATH, '//button[./span[starts-with(text(), "Тех")]]')
    ]

    # Выпадающий список городов
    CITY_DROPDOWN = (By.XPATH, '(//button[contains(@class, "dropDownMenu_arrowDown")])[2]')

    # Опция города
    CITY_OPTION = [
        (By.XPATH, '//button[./span[starts-with(text(), "Мос")]]'),
        (By.XPATH, '//button[./span[starts-with(text(), "Сан")]]'),
        (By.XPATH, '//button[./span[starts-with(text(), "Нов")]]'),
        (By.XPATH, '//button[./span[starts-with(text(), "Ека")]]'),
        (By.XPATH, '//button[./span[starts-with(text(), "Ниж")]]'),
        (By.XPATH, '//button[./span[starts-with(text(), "Каз")]]')
    ]

    # Поле "Стоимость"
    PRICE = (By.XPATH, '//input[@name="price"]')

    # Кнопка "Применить"в фильтре
    APPLY_FILTER_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Войти")]')

    # Карточка объявления
    CARD_AD_BUTTON = (By.XPATH, '//*[contains(@class, "card")]')

    # Кнопка пагинации вперед
    PAGINATION_FORWARD_BUTTON = (By.XPATH, '//button[contains(@class, "arrowButton--right undefined")]')

    # Кнопка пагинации назад
    PAGINATION_BACK_BUTTON = (By.XPATH, '//button[contains(@class, "arrowButton--left undefined")]')

    # Заголовок модального окна
    MODAL_HEADER = (By.XPATH, '//h1[contains(text(), "Войти") or contains(text(), "Зарегистрироваться") or contains(text(), "Чтобы разместить объявление, авторизуйтесь")]')

    # Поле "Введите Email"
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')

    # Граница поля "Введите Email"
    EMAIL_BORDER = (By.XPATH, '//input[@name="email"]/..')

    # Ошибка в поле "Введите Email"
    EMAIL_ERROR_MESSAGE = (By.XPATH, '//span[contains(text(), "Ошибка") or contains(text(), "Логин или пароль неверны")]')

    # Поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')

    # Граница поля "Пароль"
    PASSWORD_BORDER = (By.XPATH, '//input[@name="password"]/..')

    # Кнопка видимости пароля
    PASSWORD_VISIBLE_BUTTON = (By.XPATH, '//button[@class="eyeButton"]')

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Войти")]')

    # Кнопка "Нет аккаунта"
    NO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Нет аккаунта"]')

    # Кнопка закрытия модального окна
    MODAL_WINDOW_CLOSE_BUTTON = (By.XPATH, '(//button[contains(@class, "popUp")])[1]')

    # Граница поля "Подтверждение пароля"
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '//input[@name="submitPassword"]')

    # Поле "Подтверждение пароля"
    CONFIRM_PASSWORD_BORDER = (By.XPATH, '//input[@name="submitPassword"]/..')

    # Кнопка видимости пароля в поле "Подтверждение пароля"
    CONFIRM_PASSWORD_VISIBLE_BUTTON = (By.XPATH, '(//button[@class="eyeButton"])[2]')

    # Кнопка "Создать аккаунт"
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Создать аккаунт")]')

    # Аватар пользователя
    USER_AVATAR = (By.XPATH, '//button[@class="circleSmall"]')

    # Имя пользователя
    USER_NAME = (By.XPATH, '//h3[@class="profileText name"]')

    # Кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, '//button[@type="button" and text()="Выйти"]')

    # Поле "Имя"
    USERNAME_INPUT = (By.XPATH, '//input[(@name="name") and (@placeholder="Имя")]')

    # Кнопка "Добавить фото"
    ADD_PHOTO_BUTTON = (By.XPATH, '//button[@type="button" and contains(text(), "Добавить фото")]')

    # Кнопка "Сохранить изменения" в профиле
    SAVE_CHANGES_PROFILE_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Сохранить изменения")]')

    # Карточка избранного объявления
    CHOSEN_AD_CARD_BUTTON = (By.XPATH, '//div[./h1[contains(text(), "Избранные объявления")]]//div[contains(@class, "grid_twoColumns__HwA+w")]/div[contains(@class, "card")]')

    # Заголовки карточек избранных объявлений
    CHOSEN_AD_CARDS_TITLE = (By.XPATH, '//div[./h1[contains(text(), "Избранные объявления")]]//div[contains(@class, "about")]/h2[contains(@class, "h2")]')

    # Кнопка пагинации избранных вперед
    PAGINATION_FORWARD_CHOSEN_BUTTON = (By.XPATH, '//h1[@class="h1" and text()="Избранные объявления"]/following::div//button[contains(@class, "arrowButton--right undefined")]')

    # Кнопка пагинации избранных назад
    PAGINATION_BACK_CHOSEN_BUTTON = (By.XPATH, '//h1[@class="h1" and text()="Избранные объявления"]/following::div//button[contains(@class, "arrowButton--left undefined")]')

    # Карточка моего объявления
    MY_AD_CARD_BUTTON = (By.XPATH, '//div[./h1[contains(text(), "Мои объявления")]]//div[contains(@class, "grid_twoColumns__HwA+w")]/div[contains(@class, "card")]')

    # Заголовки карточек моих объявлений
    MY_AD_CARDS_TITLE = (By.XPATH, '//div[./h1[starts-with(text(), "Мои объявления")]]//div[contains(@class, "about")]/h2[contains(@class, "h2")]')

    # Кнопка пагинации моих объявлений вперед
    PAGINATION_FORWARD_MY_BUTTON = (By.XPATH, '//h1[@class="h1" and text()="Мои объявления"]/following::div//button[contains(@class, "arrowButton--right undefined")]')

    # Кнопка пагинации моих объявлений назад
    PAGINATION_BACK_MY_BUTTON = (By.XPATH, '//h1[@class="h1" and text()="Мои объявления"]/following::div//button[contains(@class, "arrowButton--left undefined")]')

    # поле название
    TITLE_INPUT = (By.XPATH, '//input[(@name="name") and (@placeholder="Название")]')

    # Радио-баттон "Новый"
    CONDITION_NEW_RADIO = (By.XPATH, '//label[contains(@class, "h2") and text()="Новый"]/preceding-sibling::div')

    # Радио-баттон "Б/У"
    CONDITION_OLD_RADIO = (By.XPATH, '//label[contains(@class, "h2") and text()="Б/У"]/preceding-sibling::div')

    # Поле ввода "Описание товара"
    PRODUCT_DESCRIPTION_INPUT = (By.XPATH, '//textarea[@placeholder="Описание товара"]')

    # Кнопка "Опубликовать"
    PUBLISH_AD_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Опубликовать")]')

    # Домашняя страница
    HOME = (By.XPATH, '//*[contains(@class, "homePage_homepage")]')
