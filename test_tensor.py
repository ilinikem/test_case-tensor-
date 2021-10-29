from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Чтобы скрыть браузер


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options() # Чтобы скрыть браузер
    options.add_argument('--headless') # Чтобы скрыть браузер
    browser = webdriver.Chrome(chrome_options=options) # Чтобы скрыть браузер
    link = "https://yandex.ru/"
    browser.get(link)
    browser.implicitly_wait(5)
    # browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# Проверяем наличия поля поиска
def test_searchfield(browser):
    searchfield = browser.find_element(By.XPATH, '//*[@id="text"]')
    assert searchfield, 'Элемент поле поиска не найден'
    browser.quit()

# Проверяем, что появилась таблица с подсказками (suggest) 
def test_suggest(browser):
    searchfield = browser.find_element(By.XPATH, '//*[@id="text"]')
    searchfield.send_keys('Тензор')
    browser.implicitly_wait(5)
    suggestions = browser.find_element(By.XPATH, '/html/body')
    table = suggestions.get_attribute('class')
    assert "body_search_yes" in table, 'Таблица с результатами не выведена'
    time.sleep(1)
    browser.quit()

# Проверяем, что в первых 5 результатах есть ссылка на tensor.ru
def test_link(browser):
    searchfield = browser.find_element(By.XPATH, '//*[@id="text"]')
    searchfield.send_keys('Тензор')
    time.sleep(1)
    searchfield.send_keys(Keys.ENTER)
    browser.implicitly_wait(5)
    links = browser.find_elements(By.CSS_SELECTOR, '#search-result > .serp-item a.link > b')
    items = [elem.text.strip() for elem in links[:5]]
    assert "tensor.ru" in items, 'tensor.ru отсутствует в первых 5 пунктах'
    time.sleep(1)
    browser.quit() 


# options = Options()
# options.add_argument('--headless')
# test_suggest(browser = webdriver.Chrome(chrome_options=options))
# test_suggest(browser = webdriver.Chrome())