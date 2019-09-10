# Selenium with Python Simple

### Install

pip3 install selenium

### Run

python3 file.py

#### Reference
https://stackabuse.com/getting-started-with-selenium-and-python/

#### Find elements

```python
.find_element_by_id  
.find_element_by_tag_name  
.find_element_by_class_name  
.find_element_by_name  
.find_elements_by_xpath("//tag[@attr='val']")
```

#### Executing JavaScript  

```python
driver.execute_script("script")
```

#### Saving a screenshot  

```python
driver.save_screenshot('image.png')
```

#### Sending keys  

```python
from selenium.webdriver.common.keys import Keys
search_box.send_keys(Keys.RETURN)
```

#### Wait Element  

```python
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
```


 

