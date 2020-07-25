from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
import chromedriver_binary
import webbrowser


# Open web (account 1)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 3'))
driver = webdriver.Chrome(options=options)


# メルカリのページにアクセス
sleep(1)
driver.get("https://www.mercari.com/jp/mypage/listings/in_progress/")

try:
   # 要素のクラス名を指定して取引ページの発送待ちのみURLを取得
   elms = driver.find_elements_by_class_name("mypage-item-link")
   status = driver.find_elements_by_class_name("mypage-item-body")
   i = 0
   lists = []
   for elm in elms:
      sta = status[i].text
      if '発送待ち' in sta:
         elm = elms[i].get_attribute("href")
         lists.append(elm)
      i += 1
   #取得したリンクの住所を取得
   i = 0
   for m1inf in lists:
      driver.get(lists[i])
      #クラス名を指定して要素を特定
      profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
      print(profit[6].text)
      i += 1
      sleep(1)
except Exception as e:
   print('No item')
   print(e)


#ヤフオクマイページにアクセス
sleep(1)
driver.get('https://auctions.yahoo.co.jp/closeduser/jp/show/mystatus?select=closed&hasWinner=1')
try:
   #要素のクラス名を取得して、発送状態のURLを取得する
   yoms = driver.find_elements_by_class_name("decTxt03")
   #print(yoms)
   i = 0
   lists = [] 
   for yom in yoms:
      msg = yom.find_elements_by_css_selector("a")[0]
      msgt = msg.text
      if "支払い" in msgt:
         url = msg.get_attribute("href")
         lists.append(url)
      i += 1
   #取得したリンクの住所を取得
   i = 0
   for yinf in lists:
      driver.get(lists[i])
      #クラス名を指定して落札者の情報を取得
      yname = driver.find_elements_by_css_selector(".decCnfWr")
      print(yname[2].text)
      print(yname[3].text)
      print(yname[1].text)
      yitem = driver.find_elements_by_css_selector(".decItmName")
      print(yitem[0].text)
      ypri = driver.find_elements_by_css_selector(".decPrice")
      print(ypri[0].text)
      i += 1
      sleep(1)
except Exception as e:
   print(e)


# Open web (account 2)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 2'))
driver = webdriver.Chrome(options=options)

# メルカリのページにアクセス
sleep(1)
driver.get('https://www.mercari.com/jp/mypage/listings/in_progress/')
try:
   # 要素のクラス名を指定して取引ページの発送待ちのみURLを取得
   elms = driver.find_elements_by_class_name("mypage-item-link")
   status = driver.find_elements_by_class_name("mypage-item-body")
   i = 0
   lists = []
   for elm in elms:
      sta = status[i].text
      if '発送待ち' in sta:
         elm = elms[i].get_attribute("href")
         lists.append(elm)
      i += 1
   #取得したリンクの住所を取得
   i = 0
   for m2inf in lists:
      driver.get(lists[i])
      #クラス名を指定して要素を特定
      profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
      print(profit[6].text)
      mitm = driver.find_elements_by_css_selector(".transact-info-item.bold")
      print(mitm[0].text)
      i += 1
      sleep(1)
except Exception as e:
   print(e)