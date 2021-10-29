from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Чтобы скрыть браузер
from selenium.webdriver.support import expected_conditions as EC   



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    # options = Options() # Чтобы скрыть браузер
    # options.add_argument('--headless') # Чтобы скрыть браузер
    # browser = webdriver.Chrome(chrome_options=options) # Чтобы скрыть браузер
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# Проверка, что ссылка «Картинки» присутствует на странице
def test_searchLinkImage(browser):
    link = "https://yandex.ru/"
    browser.get(link)
    browser.implicitly_wait(1)
    searchLinkImage = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a/div[2]')
    assert searchLinkImage.text == "Картинки", 'Элемента Картинки не найдено'
    browser.quit()

# Проверка, что перешли на url https://yandex.ru/images/
def test_urlImage(browser):
    link = "https://yandex.ru/"
    browser.get(link)
    browser.implicitly_wait(2)
    searchUrlImage = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a/div[2]').click()
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[1])
    url = browser.current_url
    assert 'https://yandex.ru/images/' in url, 'URL страницы отличается от https://yandex.ru/images/'
    browser.quit()

# Проверка, что	открылась 1 категория и в поиске верный текст
def test_textImage(browser):
    link = "https://yandex.ru/"
    browser.get(link)
    browser.implicitly_wait(1)
    searchurlImage = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a/div[2]').click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])
    browser.implicitly_wait(1)
    time.sleep(3)
    text = browser.find_elements(By.CLASS_NAME, 'PopularRequestList-SearchText')[0]
    image = browser.find_element(By.CLASS_NAME, 'PopularRequestList-Item_pos_0').click()
    browser.implicitly_wait(1)
    textinsearch = browser.find_element(By.TAG_NAME, 'input').get_attribute('value')
    assert text.text == textinsearch, 'Название 1-й категории и текст в строке поиска не совпадают'
    time.sleep(3)
    browser.quit()

# Проверка, что открылась 1 картинка и она видна
def test_firstImage(browser):
    link = "https://yandex.ru/"
    browser.get(link)
    browser.implicitly_wait(1)
    searchurlImage = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a/div[2]').click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])
    browser.implicitly_wait(1)
    time.sleep(1)
    text = browser.find_elements(By.CLASS_NAME, 'PopularRequestList-SearchText')[0]
    firstcategory = browser.find_element(By.CLASS_NAME, 'PopularRequestList-Item_pos_0').click()
    browser.implicitly_wait(1)
    firstImage = browser.find_element(By.CLASS_NAME, "serp-item_pos_0").click()
    time.sleep(1)
    try:
          visibilityImage = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'MMImage-Preview')))
    except:
         raise Exception('Изображение не видно')
    time.sleep(3)
    browser.quit()

# Проверка, что при нажатии кнопки вперед картинка изменяется
def test_secondImage(browser):
    link = "https://yandex.ru/"
    browser.get(link)
    browser.implicitly_wait(1)
    searchurlImage = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a/div[2]').click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])
    browser.implicitly_wait(1)
    time.sleep(1)
    text = browser.find_elements(By.CLASS_NAME, 'PopularRequestList-SearchText')[0]
    firstcategory = browser.find_element(By.CLASS_NAME, 'PopularRequestList-Item_pos_0').click()
    firstImage = browser.find_element(By.CLASS_NAME, 'serp-item_pos_0').click()
    time.sleep(2)
    firstImageUrl = browser.current_url
    secondImage = browser.find_element(By.CLASS_NAME, 'MediaViewer-ButtonNext').click()
    time.sleep(2)
    secondImageUrl = browser.current_url
    assert firstImageUrl != secondImageUrl, 'Картинка не поменялась'
    time.sleep(3)
    browser.quit()

# Проверка, что при нажатии кнопки назад картинка изменяется на предыдущее изображение
def test_returnFirstImage(browser):
    link = "https://yandex.ru/"
    browser.get(link)
    browser.implicitly_wait(1)
    searchurlImage = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a/div[2]').click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])
    browser.implicitly_wait(1)
    time.sleep(1)
    text = browser.find_elements(By.CLASS_NAME, 'PopularRequestList-SearchText')[0]
    firstcategory = browser.find_element(By.CLASS_NAME, 'PopularRequestList-Item_pos_0').click()
    firstImage = browser.find_element(By.CLASS_NAME, 'serp-item_pos_0').click()
    time.sleep(2)
    firstImageUrl = browser.current_url
    secondImage = browser.find_element(By.CLASS_NAME, 'MediaViewer-ButtonNext').click()
    time.sleep(2)
    secondImageUrl = browser.current_url
    returnImage = browser.find_element(By.CLASS_NAME, 'MediaViewer-ButtonPrev').click()
    time.sleep(2)
    returnFirstImageUrl = browser.current_url
    assert firstImageUrl == returnFirstImageUrl, 'Нажав кнопку назад, появилось другое изображение'
    browser.quit()




# options = Options()
# options.add_argument('--headless')
# test_searchLinkImage(browser = webdriver.Chrome(chrome_options=options))
# test_returnFirstImage(browser = webdriver.Chrome())