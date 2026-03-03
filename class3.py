from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://selenium-python.readthedocs.io/getting-started.html#simple-usage")

time.sleep(20)
driver.quit()

