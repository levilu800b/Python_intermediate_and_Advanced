from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Wireless-Keyboard-Mouse-Combo-Full-Sized/dp/B0C9DQPTLM/ref=sr_1_8?crid=255JWOF0XU1OT&keywords=wireless%2Bkeyboard%2Band%2Bmouse&qid=1705933215&sprefix=wirel%2Caps%2C180&sr=8-8&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is ${price_dollar}.{price_cents}")

# Search for an element by ID
# search_bar = driver.find_element(By.NAME, value:"q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value:"submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value:".documentation-widget a")
# print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="navFooter"]/div[1]/div/div[1]/ul/li[3]/a')
print(bug_link.text)


# driver.close()
driver.quit()