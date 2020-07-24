from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.option import Options
from time import sleep
import chromedriver_binary
import webbrowser


# Open web (account 1)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 3'))
driver = webdriver.Chrome(options=options)
sleep(3)

# メルカリのページにアクセス
driver.get("https://www.mercari.com/jp/mypage/listings/in_progress/")

try:
   # 要素のクラス名を指定して取引ページの全てのURLを取得
   elms = driver.find_elements_by_class_name("mypage-item-link")
   status = driver.find_elements_by_class_name("mypage-item-body")
   i = 0
   lists = []
   for elm in elms:
      sta = status[i].text
      #print(sta)
      if '発送待ち' in sta:
         elm = elms[i].get_attribute("href")
         lists.append(elm)
      i += 1
   #取得したリンクの住所を取得
   i = 0
   for list in lists:
      driver.get(lists[i])
      #クラス名を指定して要素を特定
      profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
      print(profit[6].text)
      i += 1
   
   """
   item_page = driver.find_element_by_class_name("mypage-item-link")
   print(item_page.text)
   # 要素をクリック
   item_page.click()
   sleep(3)
   # クラス名を指定して要素を特定(CSSセレクタバージョン)
   profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
   print(profit[3].text)
   print(profit[6].text)
   """
except Exception as e:
   print('No item')
   print(e)


# Open web (account 2)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 2'))
driver = webdriver.Chrome(options=options)
sleep(3)

# メルカリのページにアクセス
driver.get('https://www.mercari.com/jp/mypage/listings/in_progress/')
try:
   # 要素のクラス名を指定して取引ページの全てのURLを取得
   elms = driver.find_elements_by_class_name("mypage-item-link")
   status = driver.find_elements_by_class_name("mypage-item-body")
   i = 0
   lists = []
   for elm in elms:
      sta = status[i].text
      #print(sta)
      if '発送待ち' in sta:
         elm = elms[i].get_attribute("href")
         lists.append(elm)
      i += 1
   #取得したリンクの住所を取得
   i = 0
   for list in lists:
      driver.get(lists[i])
      #クラス名を指定して要素を特定
      profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
      print(profit[6].text)
      i += 1
except Exception as e:
   print(e)