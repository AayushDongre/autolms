from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import time
import getpass
import os
cwd = os.getcwd()

def click_all(driver,subject_nos):
    if subject_nos[0] == 0:
        subject_nos = [p for p in range(1,int(input("Enter total number of subjects:")))]


    for subject_no in subject_nos:
            
        driver.find_element_by_xpath("//tbody/tr[{}]//td[4]/a".format(subject_no)).click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        all_links = driver.find_elements_by_xpath("//li[starts-with(@id,'module')]/div/div/div[2]/div/a")

        i = 0
        for link in all_links:
            link.send_keys(Keys.CONTROL + Keys.RETURN)
            driver.switch_to.window(driver.window_handles[1])
            i = i +1
            if i == max_windows or link == all_links[len(all_links)-1]:
                time.sleep(6)
                while not i == 0:
                    driver.switch_to.window(driver.window_handles[i+1])
                    driver.close()
                    i = i - 1
                    time.sleep(0.5)
                driver.switch_to.window(driver.window_handles[1])

        driver.switch_to.window(driver.window_handles[0])



driver = webdriver.Chrome(cwd + "\\chromedriver.exe")
while True:
    driver.get("http://mydy.dypatil.edu/")

    username = input("Enter Username:")
    password = getpass.getpass("Enter Password:")
    max_windows = int(input("Enter Maximum number of windows to be opened at a time:"))
    tries = 0

    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("loginbtn").click()
    while True:
        try:
            check = driver.find_element_by_class_name("loginerrors")

        except exceptions.NoSuchElementException:
            break
        else:
            username = input("Invalid Username.Please Enter Again:")
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys(username)
            driver.find_element_by_id("loginbtn").click()


    time.sleep(2)

    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("loginbtn").click()
    while tries < 3:
        try:
            check = driver.find_element_by_class_name("loginerrors")

        except exceptions.NoSuchElementException:
            break
        else:
            password = getpass.getpass("Wrong Password.Please Enter Again:")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(password)
            driver.find_element_by_id("loginbtn").click()
        tries = tries + 1
    if tries <  3:
        break

cont = "y"
while cont == "y" or cont == "Y":

    subject_no = [0]
    while True:
        try:
            subject_no = list(map(int,input("Enter list of subject numbers or enter 0 for all subjects:").split(",")))
            break
        except ValueError:
            pass
    
    click_all(driver,subject_no)
    cont = input("Complete another subject?(y/n):")
    driver.switch_to.window(driver.window_handles[0])

driver.close()

# python D:\AAYUSH\python\programs\Selenium\mydy.py
