from selenium import webdriver
from time import sleep
import chromedriver_binary
# Open web
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 3'))
driver = webdriver.Chrome(options=options)
sleep(5)

# メルカリのページにアクセス
driver.get("https://www.mercari.com/jp/mypage/listings/in_progress/")
# 要素のクラス名を指定して要素を取得
item_page = driver.find_element_by_class_name("mypage-item-link")
print(item_page.text)

# 要素をクリック
item_page.click()
sleep(5)


# profit = driver.find_elements_by_class_name("transact-info-table-cell")
# クラス名を指定して要素を特定(CSSセレクタバージョン)
profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
print(profit[3].text)
print(profit[6].text)



#from selenium import webdriver
#from time import sleep
#import chromedriver_binary
# Open web
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 2'))
driver = webdriver.Chrome(options=options)
sleep(5)

# メルカリのページにアクセス
driver.get("https://www.mercari.com/jp/mypage/listings/in_progress/")

i = string.count("mypage-item-link")
print(i)
 
# 要素のクラス名を指定して要素を取得
item_page = driver.find_element_by_class_name("mypage-item-link")
print(item_page.text)

# 要素をクリック
item_page.click()
sleep(5)


# profit = driver.find_elements_by_class_name("transact-info-table-cell")
# クラス名を指定して要素を特定(CSSセレクタバージョン)
profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
print(profit[3].text)
print(profit[6].text)