from selenium import webdriver
from time import sleep


class instabot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.username =username
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(),'Follow')]").click()
        sleep(4)



instabot('username','pw')
