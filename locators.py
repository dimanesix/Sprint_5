AUTH_LOGIN_FORM = './/div[contains(@class, "Auth_login")]'  # Форма входа
HEADER_NAV_PANEL = './/header[contains(@class, AppHeader_header__nav)]'  # Верхняя горизонтальная навигационная панель сайта
LOGO_STELLAR_BURGERS = './/div[contains(@class, AppHeader_header__logo)]/a'  # Логотип сайта
PLACE_FOR_ERROR_PWD_MESSAGE = 'input_status_error' # Место, где появляется сообщение об ошибке при вводе некорректного пароля
ERROR_PWD_MESSAGE = 'input__error' # Сообщение о некорректном пароле

# Поля ввода в форме "Входа"
AUTH_EMAIL_FIELD = ('.//div[@class="input pr-6 pl-6 input_type_text '
                    'input_size_default"]/input[@class="text input__textfield '
                    'text_type_main-default"]')
AUTH_PASSWORD_FIELD = ('.//div[@class="input pr-6 pl-6 input_type_password input_size_default"]/input['
                       '@class="text input__textfield text_type_main-default"]')

# Поля ввода в форме "Регистрация"
REG_NAME_EMAIL_FIELD = ('.//div[@class="input pr-6 pl-6 input_type_text '
                        'input_size_default"]/input[@class="text input__textfield '
                        'text_type_main-default"]')
REG_PASSWORD_FIELD = ('.//div[@class="input pr-6 pl-6 input_type_password input_size_default"]/input['
                      '@class="text input__textfield text_type_main-default"]')

# Кнопки...
BUTTON_LOG_IN_ACCOUNT = './/button[text()="Войти в аккаунт"]'
BUTTON_LOGIN_AUTH = './/button[text()="Войти"]'
BUTTON_SET_AN_ORDER = './/button[text()="Оформить заказ"]'
BUTTON_PERSONAL_ACCOUNT = './/p[text()="Личный Кабинет"]/parent::a'
BUTTON_LOGIN_REG_FORGOT_PWD = './/a[@href="/login"]'
BUTTON_EXIT_FROM_ACCOUNT = './/button[text()="Выход"]'
BUTTON_CONSTRUCTOR = './/p[contains(@class, "AppHeader_header__linkText")][text()="Конструктор"]/parent::a'
BUTTON_REGISTER = './/button[text()="Зарегистрироваться"]'

# Разделы в конструкторе бургеров
SAUCES_SECTION = './/h2[text()="Соусы"]'
SAUCES = './/span[text()="Соусы"]/parent::div'
BREAD_SECTION = './/h2[text()="Булки"]'
BREAD = './/span[text()="Булки"]/parent::div'
TOPING_SECTION = './/h2[text()="Начинки"]'
TOPPING = './/span[text()="Начинки"]/parent::div'