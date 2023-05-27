from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.asos.com/men/summer-essentials/cat/?cid=50085')

# Load more
load_more_btn = driver.find_element(By.CSS_SELECTOR, "[data-auto-id='loadMoreProducts']")
load_more_btn.click()

titles = driver.find_elements(By.CSS_SELECTOR, 'article a div p')
prices = driver.find_elements(By.CSS_SELECTOR, 'article a > p')
images = driver.find_elements(By.CSS_SELECTOR, 'article a img')

print(titles[0].text)
print(prices[0].text)
print(images[0].get_attribute("src"))

# products = driver.find_elements(By.TAG_NAME, 'article')

# for product in products[:10]:
#     title = product.find_element(By.TAG_NAME, 'p')
#     print(title.text)
    