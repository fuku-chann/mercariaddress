from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium.webdriver.common.keys import keys
from time import sleep
import chromedriver_binary
import webbrowser


# Open web (account 1)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 3'))
driver = webdriver.Chrome(options=options)
sleep(5)

# メルカリのページにアクセス
driver.get("https://www.mercari.com/jp/mypage/listings/in_progress/")

try:
   # 要素のクラス名を指定して要素を取得
   item_page = driver.find_element_by_class_name("mypage-item-link")
   print(item_page.text)
   # 要素をクリック
   item_page.click()
   sleep(5)
   # クラス名を指定して要素を特定(CSSセレクタバージョン)
   profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
   print(profit[3].text)
   print(profit[6].text)
except Exception as e:
   print('No item')
   print(e)


# Open web (account 2)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 2'))
driver = webdriver.Chrome(options=options)
sleep(5)

# メルカリのページにアクセス
driver.get("https://www.mercari.com/jp/mypage/listings/in_progress/")
try:
   # 要素のクラス名を指定して要素を取得
   #item_page = driver.find_elements_by_class_name("mypage-item-link")
   #item_page = driver.find_element_by_class_name("mypage-item-link").find_element_by_tag_name("a").get_attribute("href")
   listOfLi = driver.find_elements_by_class_name("mypage-item-link")
   for eachLiElement in listOfLi:
      item_page = eachLiElement.get_attribute("href")   
      #print(driver.find_elements_by_class_name("mypage-item-link"))
      #item_page = driver.find_element_by_class_name("mypage-item-link")
      print(item_page)
      sleep(5)
      url = item_page
      webbrowser.open_new(url)
      # 要素をクリック
      #string.click()
      #ActionChains(driver).key_down(Keys.CONTROL).click(string).key_up(Keys.CONTROL).perform()
      # クラス名を指定して要素を特定(CSSセレクタバージョン)
      profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
      print(profit[1].text)
      #print(profit[6].text)
      # メルカリのページにアクセス
      driver.back()
      #driver.get("https://www.mercari.com/jp/mypage/listings/in_progress/")
      sleep(1)
except Exception as e:
   print('No item')
   print(e)