import pickle
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service
import time
import json
from random import random, randrange
# number of levels
n_iterations = 30

# go to mathtrainer.org
driver = webdriver.Chrome(
    '/path/to/webdriver')
driver.get('https://www.mathtrainer.org/')

time.sleep(3)

# ================================== LOGIN ==================================
signinbtn = driver.find_element_by_class_name('signin-btn')
signinbtn.click()

time.sleep(3)

googlebtn = driver.find_element_by_class_name('firebaseui-idp-google')
googlebtn.click()

time.sleep(3)

email = 'email'
login_usr = driver.find_element_by_id('identifierId')
login_usr.send_keys(email)
next_loginbtn = driver.find_element_by_id('identifierNext')
next_loginbtn.click()

time.sleep(3)

password = 'password'
login_pwd = driver.find_element_by_name('password')
login_pwd.send_keys(password)
next_pwdbtn = driver.find_element_by_id('passwordNext')
next_pwdbtn.click()

time.sleep(10)

# ================================ ALGORITHM ================================
for i in range(1, n_iterations):
    # START THE GAME
    startbtn = driver.find_element_by_id('start')

    # GET LENGTH OF LEVEL
    levelnum = driver.find_element_by_id(
        'start').get_attribute('data-questions')
    levelsdata = json.dumps(levelnum)
    levelsjson = json.loads(levelnum)
    size = len(levelsjson)

    print("===== NEW LEVEL =====")
    print("size:", size, levelnum)
    startbtn.click()

    # CALCULUS
    for i in levelsjson:
        answer = 0
        for j, k in i.items():
            num1 = int(i.get('a'))
            num2 = int(i.get('b'))
            operator = str(i.get('o'))

            if operator == '+':
                answer = num1 + num2

            elif operator == '-':
                answer = num1 - num2

            elif operator == '*':
                answer = num1 * num2

            else:
                answer = int(num1 / num2)

        answerin = driver.find_element_by_id('input')
        answerin.send_keys(answer)
        print(num1, operator, num2, "=> ", answer)
        time.sleep(random())

    time.sleep(randrange(5, 10))

time.sleep(60)
driver.quit()
