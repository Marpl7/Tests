from selenium import webdriver
import time


def Yandex_Auth(login, password):

    driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
    driver.get("https://passport.yandex.ru/auth/")

    login = driver.find_element_by_name("login")
    login.clear()
    login.send_keys(login)
    time.sleep(2)

    driver.find_element_by_tag_xpath('//button[@data-t="button:action"]').click()
    time.sleep(2)

    pswd = driver.find_element_by_name("passwd")
    pswd.send_keys(password)
    time.sleep(2)

    driver.find_element_by_xpath('//button[@data-t="button:action"]').click()
    time.sleep(5)

    driver.close()