from selenium import webdriver
from time import sleep
import chromedriver_binary
# Open web
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 1'))
driver = webdriver.Chrome(options=options)
sleep(5)
driver.get("https://www.mercari.com/jp/mypage/listings/completed/")
item_page = driver.find_element_by_class_name("mypage-item-link")
print(item_page.text)
item_page.click()
sleep(5)
profit = driver.find_elements_by_class_name("transact-info-table-cell")
print(profit[7].text)
print(profit[1].text)
print(profit[2].text)