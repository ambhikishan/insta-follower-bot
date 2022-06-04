import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver


class InstaFollower:

    def __init__(self):
        path: str = "C:/Development/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=path)
        self.username: str = "_.galactus._.gaming._"
        self.password: str = "yoyomoluhimanshu12345"
        insta = "https://www.instagram.com"

        self.driver.get(url=insta)

    def log_in(self):
        while True:
            try:
                email = self.driver.find_element_by_name("username")
                email.send_keys(self.username)
                passw = self.driver.find_element_by_name("password")
                passw.send_keys(self.password)
                break
            except:
                continue
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        while True:
            try:
                not_now = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
                not_now.click()
                break
            except:
                pass

        while True:
            try:
                now = self.driver.find_element_by_class_name('HoLwm')
                now.click()
                break
            except:
                print("'Not Now' 2 not clicked")


    def find_follower(self):
        self.driver.get("https://www.instagram.com/iskconinc/")
        time.sleep(3.0)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        all_button = self.driver.find_elements_by_css_selector("li button")
        for button in all_button:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel.click()
acc = InstaFollower()
acc.log_in()
acc.find_follower()
acc.follow()
