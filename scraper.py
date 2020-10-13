import selenium
import os,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Plural_Scrapper:
  
    path = ""
    browser = ""
    delay = 0

    def __init__(self,path):
        self.path = path

    def launchBrowser(self):
        
        chrome_driver = "/usr/bin/chromedriver" #chromedriver bin loc

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions");

        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = { 'browser':'ALL' }


        self.browser = webdriver.Chrome(chrome_driver,chrome_options=options,desired_capabilities=d)

        Browser = self.browser
        Website = self.path

        Browser.get(Website)

        print("Browser Initiated !")
        print("Loading .. " + Website+"\n", end =' ')
        time.sleep(self.delay)



    def getURLS(self):
        CourseTitleBox="course-bottom"
        CourseCLassBox="course-content-left"

        print("getting Courses Names...")
        f = open("Course.txt", "a")
       
        for element in self.browser.find_elements(By.CLASS_NAME, CourseTitleBox) :
            course_name = element.find_element_by_xpath(".//h4").text+"\n"
            f.write(course_name)
        f.close()
        print("got all Courses Names...")


        print("getting URLS...")
        f = open("links.txt", "a")
        LinkTemplate="https://app.pluralsight.com/library/courses"

       
        for element in self.browser.find_elements(By.CLASS_NAME, CourseCLassBox) :
            URL = LinkTemplate+element.find_element_by_xpath(".//a").get_attribute('href').split("/courses")[1]+"\n"
            f.write(URL)
        f.close()
        print("got all URLS...")