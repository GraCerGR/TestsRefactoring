from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSelectorException
from Exeptions import *
from CreateCard.DataCreateCard import *
import time

def test_createCard_method(browser):
    browser.get("http://127.0.0.1:5501/patient/tests/testsCreateCard.html")
    test1 = testing_current_test(browser, "Неполное тестирование", incomplete_testing_data)
    test2 = testing_current_test(browser, "Разделение на классы эквивалентновсти (без группировки) + Структурированное базисное тестирование", division_into_equivalence_classes)
    test3 = testing_current_test(browser, "Разделение на классы эквивалентновсти (с группировкой) + Структурированное базисное тестирование", division_into_equivalence_classes, True)
    test4 = testing_current_test(browser,"Угадывание ошибок", guessing_errors_data)
    test5 = testing_current_test(browser, "Классы плохих данных", сlasses_of_bad_data_data)
    test6 = testing_current_test(browser, "Классы хороших данных", сlasses_of_good_data_data)
    test7 = testing_current_test(browser, "Тестирование, основанное на потоках данных", testing_on_data_streams_data)
    if test1 and test2 and test3 and not test4 and not test5 and test6 and test7:
        return True
    else:
        return False

def login_to_create_token(USERNAME, PASSWORD):
    browser = webdriver.Chrome()
    try:
        browser.get("http://127.0.0.1:5501/login/login.html")

        email_input = browser.find_element(By.ID, 'Email')
        email_input.send_keys(USERNAME)

        password_input = browser.find_element(By.ID, 'password')
        password_input.send_keys(PASSWORD)

        login_button = browser.find_element(By.ID, 'loginButton')
        login_button.click()
        printInfo("Вход выполнен")
        return browser
    except (TimeoutException, NoSuchElementException):
        printExeption(f"Формы ввода логина, пароля и/или кнопка входа не найдена(-ы)")
        return False
    except Exception as e:
        printExeption(f"Тип ошибки: {type(e).__name__}")
        printExeption(f"Ошибка: Ошибка входа. {e}")
        return False

def clicking_on_current_patient(browser, patientName):
    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//h6[text()='{patientName}']"))
        ).click()
        printInfo("Клик на пациента выполнен")
        return True
    except (TimeoutException, NoSuchElementException):
        printExeption(f"Пациент с именем {patientName} не найден")
        return False
    except Exception as e:
        printExeption(f"Тип ошибки: {type(e).__name__}")
        printExeption(f"Ошибка: Ошибка поиска пациента. {e}")
        return False

def testing_current_test(browser, test, data, group: bool = False):
    clicking_on_current_test(browser, test)
    if not test_createCard(browser, data, group):
        printExeption(f"Тест {test} не пройден")
        print()
        return False
    printSuccess(f"Тест {test} пройден")
    print()
    return True

def test_createCard(browser, data, group: bool = False):
    try:
        card_elements = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.p-2.my-2.container2'))
        )
    except (TimeoutException, NoSuchElementException):
        printExeption(f"Элементы карточек с осмотрами не найдены")
        return False
    except Exception as e:
        printExeption(f"Тип ошибки: {type(e).__name__}")
        printExeption(f"Ошибка: Ошибка поиска карточек. {e}")
        return False

    if not len(card_elements) > 0:
        printExeption(f"Карточки осмотров не отображаются")
        return False

    for index, card in enumerate(card_elements):
        if not test_one_card(card, data[index], group):
            return False

    return True

def clicking_on_current_test(browser, test):
    browser.find_element(By.XPATH, f"//button[contains(text(), '{test}')]").click()

def test_one_card(card, data: CardInfo, group):
    try:
        WebDriverWait(card, 3).until(
            EC.presence_of_element_located((By.XPATH,
                          f"//strong[contains(text(), 'Амбулаторный осмотр')]"))
        )
        WebDriverWait(card, 3).until(
            EC.presence_of_element_located((By.XPATH,
                          f"//div[contains(@class, 'background') and contains(text(), '{data.date}')]"))
        )
        WebDriverWait(card, 3).until(
            EC.presence_of_element_located((By.XPATH,
                          f"//div[contains(text(), 'Заключение: ') and ./strong[contains(text(), '{data.conclusion}')]]"))
        )
        WebDriverWait(card, 3).until(
            EC.presence_of_element_located((By.XPATH,
                          f"//div[contains(text(), 'Основной диагноз: ') and ./strong[contains(text(), '{data.diagnosisName}')]]"))
        )
        WebDriverWait(card, 3).until(
            EC.presence_of_element_located((By.XPATH,
                          f"//div[contains(text(), 'Медицинский работник: {data.doctor}')]"))
        )
        WebDriverWait(card, 3).until(
            EC.presence_of_element_located((By.XPATH,
                          f"//div[contains(@id, '{data.id}')]"))
        )

        if (data.hasChain and data.hasNested):
            WebDriverWait(card, 3).until(
                EC.presence_of_element_located((By.XPATH,
                              f"//a[contains(@class, 'add-inspection-link') and contains(text(), 'Добавить осмотр')]"))
            )

        if group:
            if (data.hasChain) or (data.hasNested and not data.hasChain):
                WebDriverWait(card, 3).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"//button[contains(@class, 'btn btn-light') and contains(@data-bs-toggle, 'collapse') and contains(@data-bs-target, '#collapse-{data.id}') and contains(text(), '▼')]"))
                )
            if (not data.hasNested and not data.hasChain and data.previousId):
                WebDriverWait(card, 3).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"//button[contains(@class, 'btn btn-light disabled') and contains(text(), '■')]"))
                )


        printInfo(f"Карточка {data} отображается корректно")
        return True
    except (TimeoutException, NoSuchElementException):
        printExeption(f"Элемент карточки не найден")
        printExeption(f"Карточка от {data} отображается некорректно")
        return False
    except Exception as e:
        printExeption(f"Тип ошибки: {type(e).__name__}")
        printExeption(f"Ошибка: Ошибка поиска элемента карточки. {e}")
        printExeption(f"Карточка от {data} отображается некорректно")
        return False

