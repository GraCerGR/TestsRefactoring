from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSelectorException

from Exeptions import *
from UpdatePagination.DataUpdatePagination import *

import time

def test_UpdatePagination_method(browser):
    browser.get("http://127.0.0.1:5501/patient/tests/testsUpdatePagination.html")
    test1 = data_for(browser, incomplete_testing_data, "Неполное тестирование")
    test2 = data_for(browser, structured_baseline_testing, "Структурированное базисное тестирование")
    test3 = data_for(browser, testing_on_data_streams_data, "Тестирование, основанное на потоках данных")
    test4 = data_for(browser, division_into_equivalence_classes, "Разделение на классы эквивалентности")
    test5 = data_for(browser, guessing_errors_data, "Угадывание ошибок")
    test6 = data_for(browser, analysis_of_boundary_values, "Анализ граничных условий")
    test7 = data_for(browser, сlasses_of_bad_data_data, "Классы плохих данных")
    test8 = data_for(browser, сlasses_of_bad_data_data, "Классы хороших данных")


    if test1 and test2 and test3 and test4 and test5 and test6 and test7 and test8:
        return True
    else:
        return False

def data_for(browser, data, testname):
    print()
    for element in data:
        test = test_one_input(browser, element)
        browser.find_element(By.ID, 'input1').clear()
        browser.find_element(By.ID, 'input2').clear()
        if not test:
            return False
    printSuccess(f"Тест '{testname}' выполнен успешно")
    return True

def test_one_input(browser, data):
    try:
        browser.find_element(By.ID, 'input1').send_keys(f"{data[0]}")
        browser.find_element(By.ID, 'input2').send_keys(f"{data[1]}")
        browser.find_element(By.ID, 'submitButton').click()
        pagination = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//nav[@aria-label="Пример навигации по страницам"]'))
        )
    except (TimeoutException, NoSuchElementException):
        printExeption(f"Элемент карточки не найден")
        printExeption(f"Карточка от {data} отображается некорректно")
        return False
    except Exception as e:
        printExeption(f"Тип ошибки: {type(e).__name__}")
        printExeption(f"Ошибка: Ошибка поиска элемента карточки. {e}")
        printExeption(f"Карточка от {data} отображается некорректно")
        return False

    printInfo(f"Тестирование {data}")
    if not test_drawing_pagination(data, pagination):
        printExeption(f"Тестирование {data} не успешно")
        return False
    printInfo(f"Тестирование {data} успешно")
    return True

def test_drawing_pagination(data, pagination):
    children = pagination.find_elements(By.TAG_NAME, 'li')
    MAX_PAGINATION_PARAMETR = 5

    try:
        currentPageInt = int(data[0])
    except (ValueError, TypeError):
        currentPageInt = None

    try:
        maxPaginationInt = int(data[1])
    except (ValueError, TypeError):
        maxPaginationInt = None

    if (maxPaginationInt is None and currentPageInt is None) or \
        ((maxPaginationInt is not None and maxPaginationInt <= 1) or \
        (maxPaginationInt is not None and maxPaginationInt > MAX_PAGINATION_PARAMETR and currentPageInt is None)): # <<>>
        if len(children) == 2:
            return True

    if (isinstance(maxPaginationInt, int)):
        if ((maxPaginationInt <= MAX_PAGINATION_PARAMETR) and (maxPaginationInt >= 0)):
            if len(children) != maxPaginationInt + 2:
                return False
        elif (maxPaginationInt < 0):
            if len(children) != 2:
                return False
        elif (maxPaginationInt > MAX_PAGINATION_PARAMETR):
            if len(children) != MAX_PAGINATION_PARAMETR + 2:
                return False

    if (isinstance(currentPageInt, int)):
        if isinstance(maxPaginationInt, int):
            if (currentPageInt <= maxPaginationInt) and (currentPageInt > 0):
                if not searching_active_page(currentPageInt, pagination):
                    return False
            else:
                if searching_active_page(currentPageInt, pagination):
                    return False
        else:
            if not searching_active_page(currentPageInt, pagination):
                return False
    else:
        if searching_active_page(currentPageInt, pagination):
            return False

    return True


def searching_active_page(number, pagination):
    try:
        activePage = WebDriverWait(pagination, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.page-item.active'))
        )
        if activePage.text != str(number):
            printExeption(f"Элемент найден, но активна не тот номер страницы")
            return False
        return True

    except (TimeoutException, NoSuchElementException):
        printExeption(f"Элемент не найден")
        printExeption(f"Не найдена активная страница с номером '{number}'")
        return False
    except Exception as e:
        printExeption(f"Не найдена активная страница с номером '{number}'")
        printExeption(f"Тип ошибки: {type(e).__name__}")
        printExeption(f"Ошибка: Ошибка поиска элемента. {e}")
        return False