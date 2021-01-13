from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class TensorTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testYandexSearchTensor(self):
        driver = self.driver
        driver.get('https://yandex.ru/')
        assert driver.find_element_by_id('text') != 0
        searchField = driver.find_element_by_id('text')
        searchField.send_keys('Тензор')

        time.sleep(2)

        assert driver.find_element_by_class_name('mini-suggest__popup-content').text != ''
        searchField.send_keys(Keys.ENTER)

        time.sleep(2)

        links = driver.find_elements_by_xpath("//div[contains(@class,'path organic__path')]/ a/ b")
        count = 1
        for link in links:
            if (count == 5):
                break
            print(link.text)
            assert 'tensor.ru' in link.text
            count += 1

    def testYandexImages(self):
        driver = self.driver
        driver.get('https://yandex.ru/')
        assert driver.find_element_by_xpath('//*[contains(@data-id, "images")]') != 0
        driver.find_element_by_xpath('//*[contains(@data-id, "images")]').click()

        time.sleep(2)

        driver.switch_to.window(driver.window_handles[-1])
        assert 'https://yandex.ru/images/' in driver.current_url
        categoryName = driver.find_element_by_xpath('//div[contains(@class, "PopularRequestList-SearchText")]').text
        driver.find_element_by_xpath('//div[contains(@class, "PopularRequestList-SearchText")]').click()

        time.sleep(2)

        driver.switch_to.window(driver.window_handles[-1])
        assert categoryName == driver.find_element_by_xpath('//input[contains(@class, "input__control")]').get_attribute('value')
        categoryLink = driver.current_url
        driver.find_element_by_xpath('//*[contains(@class, "serp-item__link")]').click()

        time.sleep(2)

        imageLink = driver.current_url
        assert imageLink != categoryLink
        driver.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[4]/i').click()

        time.sleep(2)

        assert driver.current_url != imageLink
        driver.find_element_by_xpath('/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[1]/i').click()

        time.sleep(2)

        assert driver.current_url == imageLink

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
