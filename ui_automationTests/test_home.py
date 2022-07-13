from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\seleniumdriver\\chromedriver.exe")


driver.get("http://127.0.0.1:5000/")



driver.close()