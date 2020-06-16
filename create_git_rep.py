import sys
import os
from selenium import webdriver

"""
Uses selenium to create a git repository in github.com using chrome
"""

path = "/Users/maximilianvorbrodt/Documents/PROGRAMMING/GitRepositories/"
chromedriver = "/Users/maximilianvorbrodt/Downloads/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('https://github.com/login')


def create():
    #take in argument from bash and make directory
    folderName = str(sys.argv[1])
    os.makedirs(path + folderName)
    print (path + folderName)

    #create python button and use it to login
    #Right click on item then select inspect, copy XPath
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys('vorbrodt')
    python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
    python_button.send_keys('password')
    python_button = browser.find_elements_by_xpath("//*[@id='login']/form/div[4]/input[9]")[0]
    python_button.click()

    #go to create new repository
    browser.get('https://github.com/new')

    #add repository name
    python_button = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    python_button.send_keys(folderName)

    #make git repository private
    python_button = browser.find_elements_by_xpath("//*[@id='repository_visibility_private']")[0]
    python_button.click()

    #initialize this repository with a README
    #python_button = browser.find_elements_by_xpath("//*[@id='repository_auto_init']")[0]
    #python_button.click()

    #press "Create repository" button via css selector
    python_button = browser.find_element_by_css_selector('button.first-in-line')
    python_button.submit()

    browser.quit()


if __name__ == "__main__":
    create()

