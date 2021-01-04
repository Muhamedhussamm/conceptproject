from selenium import webdriver #@ 34an el program yerun you have to  open chromedriver.exe manually on chrome 87
from time import sleep

#lazm el account yekon m3ml4 follow l7d abl kda
class instabot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(4)
        #comment next 2 lines lw magt4 saf7et el privacy
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(4)
                for i in range(2):
            for i in range(5):
                self.driver.find_element_by_xpath(("//button[text()='Follow']")) \
                    .click()

                sleep(2)


        sleep(2)

#t2dr tegarp bl account dh ya bashmohands
#username= 'Muhamedhussamm2014@gmail.com'
#pw = 'Mido01114694188'


instabot('username','pw') # write the user name and password manually 34an tesha5l el function
