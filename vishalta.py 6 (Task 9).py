https://www.saucedemo.com/ login with the following credentials
from selenium import webdriver

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.saucedemo.com/")

# Login
username_input = driver.find_element_by_id("user-name")
password_input = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

# Fetching required information
title = driver.title
current_url = driver.current_url
page_source = driver.page_source

# Saving contents to a text file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write("Title: {}\n".format(title))
    file.write("Current URL: {}\n\n".format(current_url))
    file.write(page_source)

# Close the WebDriver
driver.quit()




