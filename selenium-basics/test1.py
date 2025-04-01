from selenium import webdriver

driver = webdriver.Chrome()
# open the target webpage
driver.get("https://www.w3schools.com/python/")
driver.maximize_window() # maximize the window
print(driver.title) # gets the title 
driver.close()