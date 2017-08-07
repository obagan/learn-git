import re
import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/bin/chromedriver.exe')

    def test_search_in_python_org(self):
        driver = webdriver.Chrome('C:/bin/chromedriver.exe')
        driver.get("http://sneh.ru/")
        self.assertIn("sneh", driver.title)

        randomName = ['Маша', 'Петя', 'Вася']
        randomEmail = ['test@test.mail.ru',
                       'testemail@test.ru',
                       'testmail@testmail.ru']
        randomQuestion = ['Как пройти в библиотеку?',
                          'Что за сайт?',
                          'Почем нынче чугун?',
                          'Может, и сюда прикрутим блокчейн?', ]

        from selenium.webdriver.common.by import By
        element = driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[4]/a')
        element.click()  # должен нажать на "Задать вопрос"

        time.sleep(2)  # задержка времени на 4 секунды

        elem = driver.find_element_by_name("name")  # должен ввести в поле данные
        elem.send_keys(random.choice(randomName))
        assert "No results found." not in driver.page_source

        time.sleep(2)

        elem = driver.find_element_by_name("contact")  # должен ввести в поле данные
        elem.send_keys(random.choice(randomEmail))
        assert "No results found." not in driver.page_source

        time.sleep(2)

        elem = driver.find_element_by_name("question")  # должен ввести в поле данные
        elem.send_keys(random.choice(randomQuestion))
        assert "No results found." not in driver.page_source

        time.sleep(2)

        element = driver.find_element_by_css_selector('button.btn-info')
        element.click()

        time.sleep(2)

        element = driver.find_element_by_css_selector('.panel-body')
        message_id = re.findall(".*№([0-9]+).*", element.text)[0]
        print(message_id)

        driver.get("http://sneh.ru/admin/sneh/feedbackform/")
        element = driver.find_element_by_id('id_username')
        element.send_keys('ezhich')
        time.sleep(2)

        element = driver.find_element_by_id('id_password')
        element.send_keys('Sdaf2508050')
        time.sleep(2)

        element = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')
        from selenium.webdriver.common.keys import Keys
        element.send_keys(Keys.ENTER)

        element = driver.find_elements_by_class_name('action-select')
        for index, a in enumerate(element):
            if a.get_attribute('value') == message_id:
                a.click()
                break

        driver.find_element_by_name('action').click()
        driver.find_element_by_css_selector('[value=delete_selected]').click()
        driver.find_element_by_name('index').click()


        # for x in element:
        # print(x)
        # break
        # a = eval(element)
        # for i in message_id:

        # a = range(element)

        # k = element.keys()
        # a = k.sort()


        #   a = element.get_attribute('value')
        #  i+=1
        # print(a)

        # message_id = re.findall(".*№([0-9]+).*", element.text)[0]


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
