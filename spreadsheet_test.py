import gspread
import json

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('mercari-284420-8a48bc1a3e9b.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = '13H4m38CC7k0-VnhkZZolPu5D1PY4Ekb1NG_-JGL2ZvQ'

#共有設定したスプレッドシートのシート1を開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

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
   #worksheetの全てのセルの情報を取得 forの外かも？
   values_list = worksheet.get_all_values()
   if not values_list == []:
      for values in values_list:
         con_values = ''.join(values)
         value = con_values.strip('\n')
   else:
      value = values_list
   for m2inf in lists:
      driver.get(lists[i])
      #クラス名を指定して要素を特定（住所）
      profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
      #クラス名を取得して要素を特定（商品名）
      mitm = driver.find_elements_by_css_selector(".transact-info-item.bold")
      #空白の行を取得する（取得を開始する行）
      lastrow = len(values_list) + 1
      #worksheetに存在しない住所のみ取得する
      if profit[6].text not in value:
        worksheet.update_cell(lastrow, 1, profit[6].text)
        worksheet.update_cell(lastrow, 2, mitm[0].text)
      i += 1
      sleep(1)
except Exception as e:
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
      #worksheetの全てのセルの情報を取得
      value = worksheet.get_all_values()
      print(value.rstrip('\n'))
      #空白の行を取得する（取得を開始する行）
      lastrow = len(value) + 1
      print(lastrow)
      #クラス名を指定して落札者の情報を取得
      yname = driver.find_elements_by_css_selector(".decCnfWr")
      worksheet.update_cell(lastrow, 1, yname[2].text)
      print(yname[2].text)
      worksheet.update_cell(lastrow, 1, yname[3].text)
      print(yname[3].text)
      worksheet.update_cell(lastrow, 1, yname[1].text)
      print(yname[1].text)
      yitem = driver.find_elements_by_css_selector(".decItmName")
      worksheet.update_cell(lastrow, 2, yitem[0].text)
      print(yitem[0].text)
      ypri = driver.find_elements_by_css_selector(".decPrice")
      worksheet.update_cell(lastrow, 3, ypri[2].text)
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
   #worksheetの全てのセルの情報を取得
   values_list = worksheet.get_all_values()
   if not values_list == []:
      for values in values_list:
         con_values = ''.join(values)
         value = con_values.strip('\n')
   else:
      value = values_list
   for m2inf in lists:
      driver.get(lists[i])
      #クラス名を指定して要素を特定（住所）
      profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
      #クラス名を取得して要素を特定（商品名）
      mitm = driver.find_elements_by_css_selector(".transact-info-item.bold")
      #空白の行を取得する（取得を開始する行）
      lastrow = len(values_list) + 1
      #worksheetに存在しない住所のみ取得する
      if profit[6].text not in value:
        worksheet.update_cell(lastrow, 1, profit[6].text)
        worksheet.update_cell(lastrow, 2, mitm[0].text)
      i += 1
      sleep(1)
except Exception as e:
   print(e)