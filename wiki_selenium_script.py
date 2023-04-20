from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time


def create_first_wiki_page():

    #Github credentials
    username = "github username"
    password = "github password"
    project_name= "project(repo)name"

    # initialize the Chrome driver
    driver = webdriver.Chrome()

    # head to github login page
    driver.get("https://github.com/login")

    # find username/email field and send the username itself to the input field
    driver.find_element("id", "login_field").send_keys(username)
    
    # find password input field and insert password as well
    driver.find_element("id", "password").send_keys(password)
    
    # click login button
    driver.find_element("name", "commit").click()
    #Lets you see something. Here 5 seconds. Can be higher, lower or nothing(deleted), free of choice.
    time.sleep(5)
    
    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'") 
    )
    driver.get(f"https://github.com/{username}/{project_name}")

    # Maximize size of window
    driver.maximize_window()
    #Lets you see something. Here 5 seconds. Can be higher, lower or nothing(deleted), free of choice.
    time.sleep(5)

    # find setting tab and click on it
    settings =driver.find_element(By.ID, "settings-tab").click()
    #Lets you see something. Here 5 seconds. Can be higher, lower or nothing(deleted), free of choice.
    time.sleep(5)

    # find "Restrict editing to collaborators only" under Features/Wikis and unmark
    restrict_edit= driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/div[2]/div/div/div/div[4]/form[1]/div[1]/div/div/label").click()
    
    # Navigate to wiki-tab and click on it
    clickable_wiki = driver.find_element(By.ID, "wiki-tab").click()
    time.sleep(5)

    # Navigate to "create first page" and click on it
    clickable_Createfirstpage = driver.find_element(By.XPATH, "//html/body/div[1]/div[6]/div/main/turbo-frame/div/div/div/a/span/span").click()
    #Lets you see something. Here 5 seconds. Can be higher, lower or nothing(deleted), free of choice.
    time.sleep(5)

    # find "save" and click on it.
    clickable_savepage = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/div[2]/div/form/div[4]/button").click()
    #Lets you see something. Here 5 seconds. Can be higher, lower or nothing(deleted), free of choice.
    time.sleep(5)
create_first_wiki_page()