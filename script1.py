from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.headless = True
EXE_PATH = './driver/chromedriver'

# driver = webdriver.Chrome(executable_path=EXE_PATH)
driver = webdriver.Chrome(executable_path=EXE_PATH, chrome_options=options)
driver.implicitly_wait(30)
driver.maximize_window()



driver.get('https://python.org')

print(driver.title)

driver.close()