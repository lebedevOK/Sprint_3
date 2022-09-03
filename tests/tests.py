from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

class Test_Registration:
    def test_registration_successful(self):
        base_part = "a_lebedev"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        email = f"{base_part}{random_part}@{domain}"

        # Регистрация успешна
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]').click()
        driver.find_element(by=By.XPATH, value='//a[contains(text(),"Зарегистрироваться")]').click()
        driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(base_part)
        driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")
        WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        time.sleep(3)
        if driver.current_url == "https://stellarburgers.nomoreparties.site/login":
            print("Registration successful")
        else:
            print("Incorrect password, user not registered")
        print(email)

        driver.quit()

    def test_registration_incorrect_password(self):
        base_part = "a_lebedev"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        email = f"{base_part}{random_part}@{domain}"

        # Регистрация / некорректный пароль
        driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(base_part)
        driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("12345")
        WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        time.sleep(2)
        error_text = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')
        if error_text.text == 'Некорректный пароль':
            print("Incorrect password, user not registered")
        else:
            print("Registration successful")
        driver.quit()

class Entry_exit:
    def test_login_button(self):
        # Авторизация / вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]').click()
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]').send_keys(
            "a_lebedev1977@example.com")
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")
        WebDriverWait(driver, 2)
        driver.find_element(by=By.XPATH, value='//button[contains(text(),"Войти")]').click()

        time.sleep(3)
        order_button = driver.find_element(by=By.XPATH,
                                           value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]')

        if order_button.text == "Оформить заказ":
            print("Authorization successful")
        else:
            print("Authorization failed")
        driver.quit()

    def test_login_personal_area(self):
        # Авторизация / вход через кнопку «Личный кабинет»
        driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/a[1]/p[1]').click()
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]').send_keys(
            "a_lebedev1977@example.com")
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")
        WebDriverWait(driver, 2)
        driver.find_element(by=By.XPATH, value='//button[contains(text(),"Войти")]').click()

        time.sleep(3)
        order_button = driver.find_element(by=By.XPATH,
                                           value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]')

        if order_button.text == "Оформить заказ":
            print("Authorization successful")
        else:
            print("Authorization failed")
        driver.quit()

    def test_registration_form(self):
        # Авторизация / вход через кнопку в форме регистрации
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]').click()
        driver.find_element(by=By.XPATH, value='//a[contains(text(),"Зарегистрироваться")]').click()
        driver.find_element(by=By.XPATH, value='//a[contains(text(),"Войти")]').click()
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]').send_keys(
            "a_lebedev1977@example.com")
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")
        WebDriverWait(driver, 2)
        driver.find_element(by=By.XPATH, value='//button[contains(text(),"Войти")]').click()

        time.sleep(3)
        order_button = driver.find_element(by=By.XPATH,
                                           value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]')

        if order_button.text == "Оформить заказ":
            print("Authorization successful")
        else:
            print("Authorization failed")
        driver.quit()

    def test_forgot_password_form(self):
        # Авторизация / вход через кнопку в форме восстановления пароля
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]').click()
        driver.find_element(by=By.XPATH, value='//a[contains(text(),"Восстановить пароль")]').click()
        driver.find_element(by=By.XPATH, value='//a[contains(text(),"Войти")]').click()
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]').send_keys(
            "a_lebedev1977@example.com")
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")
        WebDriverWait(driver, 2)
        driver.find_element(by=By.XPATH, value='//button[contains(text(),"Войти")]').click()

        time.sleep(3)
        order_button = driver.find_element(by=By.XPATH,
                                           value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]')

        if order_button.text == "Оформить заказ":
            print("Authorization successful")
        else:
            print("Authorization failed")
        driver.quit()

    def test_log_out(self):
        # Выход из аккаунта
        driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/a[1]/p[1]').click()
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]').send_keys(
            "a_lebedev1977@example.com")
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")
        WebDriverWait(driver, 2)
        driver.find_element(by=By.XPATH, value='//button[contains(text(),"Войти")]').click()
        driver.find_element(by=By.XPATH, value='//p[contains(text(),"Личный Кабинет")]').click()
        time.sleep(3)
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/nav[1]/ul[1]/li[3]/button[1]').click()

        time.sleep(3)
        logout = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/h2[1]')

        if logout.text == "Вход":
            print("Logout is correct")
        else:
            print("Logout is not correct")

        driver.quit()

class Page_navigation:

    def test_go_to_personal_account(self):
        # Переход в личный кабинет - отображение профиля
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]').click()
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]').send_keys(
            "a_lebedev1977@example.com")
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")
        WebDriverWait(driver, 2)
        driver.find_element(by=By.XPATH, value='//button[contains(text(),"Войти")]').click()
        driver.find_element(by=By.XPATH, value='//p[contains(text(),"Личный Кабинет")]').click()
        time.sleep(3)

        if driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile":
            print("Profile displayed")
        else:
            print("Profile unavailable")
        driver.quit()

    def test_from_account_to_constructor(self):
        # Переход из аккаунта в конструктор
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]').click()
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]').send_keys(
            "a_lebedev1977@example.com")
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")
        WebDriverWait(driver, 2)
        driver.find_element(by=By.XPATH, value='//button[contains(text(),"Войти")]').click()
        driver.find_element(by=By.XPATH, value='//p[contains(text(),"Личный Кабинет")]').click()
        driver.find_element(by=By.XPATH, value='//p[contains(text(),"Конструктор")]').click()
        time.sleep(2)

        constructor_button = driver.find_element(by=By.XPATH,
                                                 value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/h1[1]')
        if constructor_button.text == "Соберите бургер":
            print("The constructor is shown")
        else:
            print("Constructor not available")
        driver.quit()

    def test_from_account_by_logo(self):
        # Переход из аккаунта в конструктор по логотипу
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]').click()
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]').send_keys(
            "a_lebedev1977@example.com")
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")
        WebDriverWait(driver, 2)
        driver.find_element(by=By.XPATH, value='//button[contains(text(),"Войти")]').click()
        driver.find_element(by=By.XPATH, value='//p[contains(text(),"Личный Кабинет")]').click()
        driver.find_element(by=By.XPATH, value='//header/nav[1]/div[1]/a[1]/*[1]').click()
        time.sleep(2)

        constructor_button = driver.find_element(by=By.XPATH,
                                                 value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/h1[1]')
        if constructor_button.text == "Соберите бургер":
            print("The constructor is shown")
        else:
            print("Constructor not available")
        driver.quit()

    def test_toppings_are_displayed(self):
        # Начинки отображаются
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[3]/span[1]').click()
        time.sleep(3)
        toppings = driver.find_element(by=By.XPATH,
                                       value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/h2[3]')

        if toppings.is_displayed() == True:
            print("Toppings are displayed")
        else:
            print("Toppings are not displayed")

        driver.quit()

    def test_sauces_are_displayed(self):
        # Соусы отображаются
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/span[1]').click()
        time.sleep(3)
        sauces = driver.find_element(by=By.XPATH,
                                     value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/h2[2]')

        if sauces.is_displayed() == True:
            print("Sauces are displayed")
        else:
            print("Sauces are not displayed")

        driver.quit()

    def test_buns_are_displayed(self):
        # Булки отображаются
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/span[1]').click()
        driver.find_element(by=By.XPATH,
                            value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[1]/span[1]').click()
        time.sleep(3)
        buns = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/h2[1]')

        if buns.is_displayed() == True:
            print("Buns are displayed")
        else:
            print("Buns are not displayed")

        driver.quit()
