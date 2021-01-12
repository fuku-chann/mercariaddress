import gspread
import json
#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 
#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/masa/dys-mercari/mercariaddress/mercari-284420-8a48bc1a3e9b.json', scope)
#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)
#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = '13H4m38CC7k0-VnhkZZolPu5D1PY4Ekb1NG_-JGL2ZvQ'
#共有設定したスプレッドシートのシート1を開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
#import chromedriver_binary
import webbrowser
from datetime import datetime as dt

#ワークシートの値を全てクリアする
worksheet.clear()

def mersta(status, lists):
   i = 0
   for elm in elms:
      sta = status[i].text
      if '発送待ち' in sta:
         elm = elms[i].get_attribute("href")
         lists.append(elm)
      i += 1
   return lists

def mercon_values():
   #worksheetの全てのセルの情報を取得
   values_list = worksheet.get_all_values()
   i = 0
   for minf in lists:
      driver.get(lists[i])
      #クラス名を指定して要素を特定（住所）
      profit = driver.find_elements_by_css_selector("ul.transact-info-table-cell")
      #クラス名を取得して要素を特定（商品名）
      mitm = driver.find_elements_by_css_selector(".transact-info-item.bold")
      #空白の行を取得する（取得を開始する行）
      lastrow = len(values_list) + 1 + i
      worksheet.update_cell(lastrow, 1, profit[6].text)
      worksheet.update_cell(lastrow, 2, "M " + mitm[0].text)
      i += 1
      sleep(1)

def json_serial(obj):
   if isinstance(obj, (dt)):
      return obj.isoformat()
   raise TypeError ("Type %s not serializable" % type(obj))

# Open web (account 1)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 3'))

try:
   driver = webdriver.Chrome(options=options, executable_path='/Users/masa/bin/chromedriver')
   sleep(1)
   driver.get("https://www.mercari.com/jp/mypage/listings/in_progress/") # メルカリにアクセス
   # 要素のクラス名を指定して取引ページの発送待ちのみURLを取得
   elms = driver.find_elements_by_class_name("mypage-item-link")
   status = driver.find_elements_by_class_name("mypage-item-body")
   lists = []
   mersta(status, lists)
   mercon_values()

   #ヤフオクマイページにアクセス
   sleep(1)
   driver.get('https://auctions.yahoo.co.jp/closeduser/jp/show/mystatus?select=closed&hasWinner=1')
   #要素のクラス名を取得して、発送状態のURLを取得する
   yoms3 = driver.find_elements_by_class_name("decTxt03")
   yoms1 = driver.find_elements_by_class_name("decTxt01")
   i = 0
   lists = [] 
   for yom3 in yoms3:
      msg3 = yom3.find_elements_by_css_selector("a")[0]
      msgt3 = msg3.text
      if "支払いが完了しました" in msgt3:
         url = msg3.get_attribute("href")
         lists.append(url)
      i += 1
   for yom1 in yoms1:
      msg1 = yom1.find_elements_by_css_selector("a")[0]
      msgt1 = msg1.text
      if "取引" in msgt1:
         url = msg1.get_attribute("href")
         lists.append(url)
      i += 1
   #取得したリンクの住所を取得
   i = 0
   j = 0
   #worksheetの全てのセルの情報を取得
   values_list = worksheet.get_all_values()
   for yinf in lists:
      driver.get(lists[i])
      #空白の行を取得する（取得を開始する行）
      lastrow = len(values_list) + 1 + j
      #クラス名を指定して落札者の情報を取得
      yname = driver.find_elements_by_css_selector(".decCnfWr")
      yitem = driver.find_elements_by_css_selector(".decItmName")
      ypri = driver.find_elements_by_css_selector(".decPrice")
      yspst = driver.find_elements_by_class_name("acMdStatusImage__chargeText")
      if yspst[2].text == "あなた":
         worksheet.update_cell(lastrow, 1, yname[2].text + '\n' + yname[3].text + '\n' + yname[1].text + " 様")
         worksheet.update_cell(lastrow, 2, "Y " + yitem[0].text)
         j += 1
      i += 1
      sleep(1)

   # ラクマにアクセス
   sleep(1)
   driver.get("https://fril.jp/sell#trading")
   sleep(1)
   # 要素のクラス名を指定して取引ページの発送待ちのみURLを取得
   relms = driver.find_elements_by_class_name("media")
   i = 0
   lists = []
   for relm in relms:
      relmt = relm.text
      if "商品の発送" in relmt:
         rmsga = relm.find_element_by_css_selector("a")
         url = rmsga.get_attribute("href")
         lists.append(url)
      i += 1
   i = 0
   #worksheetの全てのセルの情報を取得
   values_list = worksheet.get_all_values()
   #con_values = ''.join(sum(values_list,[]))
   for rinf in lists:
      driver.get(lists[i])
      #空白の行を取得する（取得を開始する行）
      lastrow = len(values_list) + 1 + i
      #クラス名を指定して要素を特定（住所）
      profit = driver.find_elements_by_css_selector('.col.s12')
      #クラス名を取得して要素を特定（商品名）
      ritm = driver.find_elements_by_css_selector('.item_name')
      #空白の行を取得する（取得を開始する行）
      lastrow = len(values_list) + 1 + i
      worksheet.update_cell(lastrow, 1, profit[7].text)
      worksheet.update_cell(lastrow, 2, "R " + ritm[0].text)
      i += 1
      sleep(1)
except Exception as e:
   print(e)
   driver.quit()
sleep(1)
#全てのウインドウを閉じる
driver.quit()
print('A-8')

# Open web (account 2)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 2'))
print('B-1')

try:
   driver = webdriver.Chrome(options=options, executable_path='/Users/masa/bin/chromedriver')
   # メルカリにアクセス
   driver.get('https://www.mercari.com/jp/mypage/listings/in_progress/')
   # 要素のクラス名を指定して取引ページの発送待ちのみURLを取得
   elms = driver.find_elements_by_class_name("mypage-item-link")
   status = driver.find_elements_by_class_name("mypage-item-body")
   lists = []
   mersta(status, lists)
   mercon_values()
except Exception as e:
   print(e)
   driver.quit()
time_now = json.dumps(dt.now(), default=json_serial)
sleep(1)
#全てのウインドウを閉じる
driver.quit()
print('last', dt.now())
worksheet.update_cell(1, 5, time_now)