from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
import chromedriver_binary
import webbrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

# 入力（共通部分）
def sct():
   select = Select(cateElement)
   select.select_by_index(indexNum)
# ダイソン共通
def ctd(): 
   # カテゴリー
   cateElement = driver.find_elements_by_css_selector("select[name=categoryId]")[0]
   indexNum= 8
   select = Select(cateElement)
   select.select_by_index(indexNum)
   cateElement = driver.find_elements_by_css_selector("select[name=categoryId]")[1]
   indexNum= 9
   select = Select(cateElement)
   select.select_by_index(indexNum)
   cateElement = driver.find_elements_by_css_selector("select[name=categoryId]")[2]
   indexNum= 7
   select = Select(cateElement)
   select.select_by_index(indexNum)
   # ブランド
   inputElement2 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[1].find_element_by_css_selector("input")
   inputElement2.send_keys("ダイソン")
# メルカリ共通
def mc():
   # 商品の状態
   cateElement = driver.find_element_by_css_selector("select[name=itemCondition")
   indexNum= 1
   select = Select(cateElement)
   select.select_by_index(indexNum)
   # 配送料の負担
   cateElement = driver.find_element_by_css_selector("select[name=shippingPayer")
   indexNum= 1
   select = Select(cateElement)
   select.select_by_index(indexNum)
   # 配送の方法
   cateElement = driver.find_element_by_css_selector("select[name=shippingMethod")
   indexNum= 6
   select = Select(cateElement)
   select.select_by_index(indexNum)
   # 配送元の地域
   cateElement = driver.find_element_by_css_selector("select[name=shippingFromArea")
   indexNum= 12
   select = Select(cateElement)
   select.select_by_index(indexNum)
   # 発送までの日数
   cateElement = driver.find_element_by_css_selector("select[name=shippingDuration")
   indexNum= 1
   select = Select(cateElement)
   select.select_by_index(indexNum)
def itm1(): #ダイソン掃除機 タイヤ4個+テフロンテープ+トルクスドライバー３本セット
   # 画像をアップロード
   driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/masa/Pictures/torx/torxset.jpeg \n /Users/masa/Pictures/dyson/tire4.jpeg \n /Users/masa/Pictures/dyson/tape.jpeg \n /Users/masa/Pictures/torx/torxdriver.jpeg \n /Users/masa/Pictures/dyson/moeterhead.jpeg \n /Users/masa/Pictures/dyson/morterheadback.jpeg")
   # 商品名
   inputElement1 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[0].find_element_by_css_selector("input")
   inputElement1.send_keys("ダイソン掃除機 タイヤ４個＋テフロンテープ＋トルクスドライバー３本セット")
   # 商品の説明
   inputElement1 = driver.find_elements_by_class_name("style_body__1OP1S")[2].find_element_by_css_selector("textarea")
   inputElement1.send_keys("\
   【商品紹介】\n画像の2～4枚目が商品になります。ダイソンモーターヘッドの裏側に付いているタイヤと工具です。\nタイヤが劣化すると約１年ほどでフローリングや畳が傷つくことがあります。そのため、定期的に交換する必要があります。\
   \n\n【交換方法】\n交換方法などブログで詳しく紹介していますので、必ず購入前にご確認ください。\nブラウザでURLを入力すると検索できます。(URL：fuku-channnel.com)\nブログが検索できたら、サイト内検索で「ダイソン」と入力下さい。\
   \n\n【対象機種】\n実績機種は、DC35, DC48, DC59, DC62, V6です。\nその他の機種でも適合する可能性があります。(その他の機種でタイヤ交換をご検討されている方は次の保証内容をご確認ください。)\
   \n\n【保証内容】\n対象機種以外で交換をご検討されている場合、下記2点をご対応いただくことで保証が適応されることがあります。(対象機種は保証が適用されます)\n1. コメントにてご利用の機種をご連絡ください。\n2. ヘッドの裏の写真(タイヤ部分がわかる写真)を出品下さい。(価格は9,999,999としてください。)\nこちらで取り付けできると判断した場合のみ、保証が適応されます。保証が適応された場合、万が一取り付けできなかったら返金いたしますので、その旨ご連絡ください。\
   \n\n【交換頻度】\n１年以内の交換をおすすめしています。\n【タイヤのサイズ】\n外径: 10 mm\n内径: 3 mm\n幅: 4 mm\nシャフトにシールを巻くことを前提にしています。詳しくは上記ブログ（タイヤの取り付け方）をご覧下さい。\
   \n\n【現状のメーカー修理】\nメーカーで修理依頼すると、購入から2年以上経過すると最低5000円の工賃が発生します。\
   \n\n【最後に】\nタイヤは簡単に交換できるので、DIYで行うことをおすすめしています。(機種によって右後輪の取り外しが困難な場合があります)\nメーカーから部品だけの購入が不可と言われたため、自分で作成したものを出品しています。\n実績多数ありますが、購入後のトラブルには責任を負えません。ご了承いただける方のみご購入下さい。\n最近、ご購入者様からお褒めの言葉を多く頂いております。モチベーションの向上に繋がりますので、評価の方にもコメントいただけたら幸いです。")
   # 販売価格
   inputElement3 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[2].find_element_by_css_selector("input")
   inputElement3.send_keys("680")
def itm2(): #ダイソン掃除機 タイヤ4個+テフロンテープ+シャフト４本セット
   # 画像をアップロード
   driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/masa/Pictures/dyson/shaftset.jpeg \n /Users/masa/Pictures/dyson/tire4.jpeg \n /Users/masa/Pictures/dyson/tape.jpeg \n /Users/masa/Pictures/dyson/shaft.jpeg \n /Users/masa/Pictures/dyson/moeterhead.jpeg \n /Users/masa/Pictures/dyson/morterheadback.jpeg")
   # 商品名
   inputElement1 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[0].find_element_by_css_selector("input")
   inputElement1.send_keys("ダイソン掃除機 タイヤ４個＋テフロンテープ＋シャフト４本セット")
   # 商品の説明
   inputElement1 = driver.find_elements_by_class_name("style_body__1OP1S")[2].find_element_by_css_selector("textarea")
   inputElement1.send_keys("\
   【商品紹介】\n画像の2～4枚目が商品になります。ダイソンモーターヘッドの裏側に付いているタイヤと部品です。\nタイヤが劣化すると約１年ほどでフローリングや畳が傷つくことがあります。そのため、定期的に交換する必要があります。\
   \n\n【交換方法】\n交換方法などブログで詳しく紹介していますので、必ず購入前にご確認ください。\nブラウザでURLを入力すると検索できます。(URL：fuku-channnel.com)\nブログが検索できたら、サイト内検索で「ダイソン」と入力下さい。\
   \n\n【対象機種】\n実績機種は、DC35, DC48, DC59, DC62, V6です。\nその他の機種でも適合する可能性があります。(その他の機種でタイヤ交換をご検討されている方は次の保証内容をご確認ください。)\
   \n\n【保証内容】\n対象機種以外で交換をご検討されている場合、下記2点をご対応いただくことで保証が適応されることがあります。(対象機種は保証が適用されます)\n1. コメントにてご利用の機種をご連絡ください。\n2. ヘッドの裏の写真(タイヤ部分がわかる写真)を出品下さい。(価格は9,999,999としてください。)\nこちらで取り付けできると判断した場合のみ、保証が適応されます。保証が適応された場合、万が一取り付けできなかったら返金いたしますので、その旨ご連絡ください。\
   \n\n【交換頻度】\n１年以内の交換をおすすめしています。\n【タイヤのサイズ】\n外径: 10 mm\n内径: 3 mm\n幅: 4 mm\nシャフトにシールを巻くことを前提にしています。詳しくは上記ブログ（タイヤの取り付け方）をご覧下さい。\
   \n\n【現状のメーカー修理】\nメーカーで修理依頼すると、購入から2年以上経過すると最低5000円の工賃が発生します。\
   \n\n【最後に】\nタイヤは簡単に交換できるので、DIYで行うことをおすすめしています。(機種によって右後輪の取り外しが困難な場合があります)\nメーカーから部品だけの購入が不可と言われたため、自分で作成したものを出品しています。\n実績多数ありますが、購入後のトラブルには責任を負えません。ご了承いただける方のみご購入下さい。\n最近、ご購入者様からお褒めの言葉を多く頂いております。モチベーションの向上に繋がりますので、評価の方にもコメントいただけたら幸いです。")
   # 販売価格
   inputElement3 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[2].find_element_by_css_selector("input")
   inputElement3.send_keys("680")
def itm3(): #ダイソン掃除機 タイヤ4個+テフロンテープ+シャフト４本+トルクスドライバー3本
   # 画像をアップロード
   driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/masa/Pictures/dyson/4set.jpeg \n /Users/masa/Pictures/dyson/tire4.jpeg \n /Users/masa/Pictures/dyson/tape.jpeg \n /Users/masa/Pictures/torx/torxdriver.jpeg \n /Users/masa/Pictures/dyson/shaft.jpeg \n /Users/masa/Pictures/dyson/moeterhead.jpeg \n /Users/masa/Pictures/dyson/morterheadback.jpeg")
   # 商品名
   inputElement1 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[0].find_element_by_css_selector("input")
   inputElement1.send_keys("ダイソン掃除機 タイヤ4個+テフロンテープ+シャフト４本+トルクスドライバー3本")
   # 商品の説明
   inputElement1 = driver.find_elements_by_class_name("style_body__1OP1S")[2].find_element_by_css_selector("textarea")
   inputElement1.send_keys("\
   【商品紹介】\n画像の2～5枚目が商品になります。ダイソンモーターヘッドの裏側に付いているタイヤと部品と工具です。\nタイヤが劣化すると約１年ほどでフローリングや畳が傷つくことがあります。そのため、定期的に交換する必要があります。\
   \n\n【交換方法】\n交換方法などブログで詳しく紹介していますので、必ず購入前にご確認ください。\nブラウザでURLを入力すると検索できます。(URL：fuku-channnel.com)\nブログが検索できたら、サイト内検索で「ダイソン」と入力下さい。\
   \n\n【対象機種】\n実績機種は、DC35, DC48, DC59, DC62, V6です。\nその他の機種でも適合する可能性があります。(その他の機種でタイヤ交換をご検討されている方は次の保証内容をご確認ください。)\
   \n\n【保証内容】\n対象機種以外で交換をご検討されている場合、下記2点をご対応いただくことで保証が適応されることがあります。(対象機種は保証が適用されます)\n1. コメントにてご利用の機種をご連絡ください。\n2. ヘッドの裏の写真(タイヤ部分がわかる写真)を出品下さい。(価格は9,999,999としてください。)\nこちらで取り付けできると判断した場合のみ、保証が適応されます。保証が適応された場合、万が一取り付けできなかったら返金いたしますので、その旨ご連絡ください。\
   \n\n【交換頻度】\n１年以内の交換をおすすめしています。\n【タイヤのサイズ】\n外径: 10 mm\n内径: 3 mm\n幅: 4 mm\nシャフトにシールを巻くことを前提にしています。詳しくは上記ブログ（タイヤの取り付け方）をご覧下さい。\
   \n\n【現状のメーカー修理】\nメーカーで修理依頼すると、購入から2年以上経過すると最低5000円の工賃が発生します。\
   \n\n【最後に】\nタイヤは簡単に交換できるので、DIYで行うことをおすすめしています。(機種によって右後輪の取り外しが困難な場合があります)\nメーカーから部品だけの購入が不可と言われたため、自分で作成したものを出品しています。\n実績多数ありますが、購入後のトラブルには責任を負えません。ご了承いただける方のみご購入下さい。\n最近、ご購入者様からお褒めの言葉を多く頂いております。モチベーションの向上に繋がりますので、評価の方にもコメントいただけたら幸いです。")
   # 販売価格
   inputElement3 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[2].find_element_by_css_selector("input")
   inputElement3.send_keys("880")
def itm4(): #ダイソン掃除機 タイヤ4個+テフロンテープセット
   # 画像をアップロード
   driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/masa/Pictures/dyson/tire4set.JPG \n /Users/masa/Pictures/dyson/tire4.jpeg \n /Users/masa/Pictures/dyson/tape.jpeg \n /Users/masa/Pictures/dyson/moeterhead.jpeg \n /Users/masa/Pictures/dyson/morterheadback.jpeg")
   # 商品名
   inputElement1 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[0].find_element_by_css_selector("input")
   inputElement1.send_keys("ダイソン掃除機 タイヤ4個+テフロンテープセット")
   # 商品の説明
   inputElement1 = driver.find_elements_by_class_name("style_body__1OP1S")[2].find_element_by_css_selector("textarea")
   inputElement1.send_keys("\
   【商品紹介】\n画像の2～3枚目が商品になります。ダイソンモーターヘッドの裏側に付いているタイヤです。\nタイヤが劣化すると約１年ほどでフローリングや畳が傷つくことがあります。そのため、定期的に交換する必要があります。\
   \n\n【交換方法】\n交換方法などブログで詳しく紹介していますので、必ず購入前にご確認ください。\nブラウザでURLを入力すると検索できます。(URL：fuku-channnel.com)\nブログが検索できたら、サイト内検索で「ダイソン」と入力下さい。\
   \n\n【対象機種】\n実績機種は、DC35, DC48, DC59, DC62, V6です。\nその他の機種でも適合する可能性があります。(その他の機種でタイヤ交換をご検討されている方は次の保証内容をご確認ください。)\
   \n\n【保証内容】\n対象機種以外で交換をご検討されている場合、下記2点をご対応いただくことで保証が適応されることがあります。(対象機種は保証が適用されます)\n1. コメントにてご利用の機種をご連絡ください。\n2. ヘッドの裏の写真(タイヤ部分がわかる写真)を出品下さい。(価格は9,999,999としてください。)\nこちらで取り付けできると判断した場合のみ、保証が適応されます。保証が適応された場合、万が一取り付けできなかったら返金いたしますので、その旨ご連絡ください。\
   \n\n【交換頻度】\n１年以内の交換をおすすめしています。\n【タイヤのサイズ】\n外径: 10 mm\n内径: 3 mm\n幅: 4 mm\nシャフトにシールを巻くことを前提にしています。詳しくは上記ブログ（タイヤの取り付け方）をご覧下さい。\
   \n\n【現状のメーカー修理】\nメーカーで修理依頼すると、購入から2年以上経過すると最低5000円の工賃が発生します。\
   \n\n【最後に】\nタイヤは簡単に交換できるので、DIYで行うことをおすすめしています。(機種によって右後輪の取り外しが困難な場合があります)\nメーカーから部品だけの購入が不可と言われたため、自分で作成したものを出品しています。\n実績多数ありますが、購入後のトラブルには責任を負えません。ご了承いただける方のみご購入下さい。\n最近、ご購入者様からお褒めの言葉を多く頂いております。モチベーションの向上に繋がりますので、評価の方にもコメントいただけたら幸いです。")
   # 販売価格
   inputElement3 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[2].find_element_by_css_selector("input")
   inputElement3.send_keys("600")
def itm5(): #ダイソン掃除機 タイヤ4個
   # 画像をアップロード
   driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/masa/Pictures/dyson/tireimage.png \n /Users/masa/Pictures/dyson/tire4.jpeg \n /Users/masa/Pictures/dyson/moeterhead.jpeg \n /Users/masa/Pictures/dyson/morterheadback.jpeg")
   # 商品名
   inputElement1 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[0].find_element_by_css_selector("input")
   inputElement1.send_keys("ダイソン掃除機 タイヤ4個")
   # 商品の説明
   inputElement1 = driver.find_elements_by_class_name("style_body__1OP1S")[2].find_element_by_css_selector("textarea")
   inputElement1.send_keys("\
   【商品紹介】\n画像の2枚目が商品になります。ダイソンモーターヘッドの裏側に付いているタイヤです。\nタイヤが劣化すると約１年ほどでフローリングや畳が傷つくことがあります。そのため、定期的に交換する必要があります。\
   \n\n【交換方法】\n交換方法などブログで詳しく紹介していますので、必ず購入前にご確認ください。\nブラウザでURLを入力すると検索できます。(URL：fuku-channnel.com)\nブログが検索できたら、サイト内検索で「ダイソン」と入力下さい。\
   \n\n【対象機種】\n実績機種は、DC35, DC48, DC59, DC62, V6です。\nその他の機種でも適合する可能性があります。(その他の機種でタイヤ交換をご検討されている方は次の保証内容をご確認ください。)\
   \n\n【保証内容】\n対象機種以外で交換をご検討されている場合、下記2点をご対応いただくことで保証が適応されることがあります。(対象機種は保証が適用されます)\n1. コメントにてご利用の機種をご連絡ください。\n2. ヘッドの裏の写真(タイヤ部分がわかる写真)を出品下さい。(価格は9,999,999としてください。)\nこちらで取り付けできると判断した場合のみ、保証が適応されます。保証が適応された場合、万が一取り付けできなかったら返金いたしますので、その旨ご連絡ください。\
   \n\n【交換頻度】\n１年以内の交換をおすすめしています。\n【タイヤのサイズ】\n外径: 10 mm\n内径: 3 mm\n幅: 4 mm\nシャフトにシールを巻くことを前提にしています。詳しくは上記ブログ（タイヤの取り付け方）をご覧下さい。\
   \n\n【現状のメーカー修理】\nメーカーで修理依頼すると、購入から2年以上経過すると最低5000円の工賃が発生します。\
   \n\n【最後に】\nタイヤは簡単に交換できるので、DIYで行うことをおすすめしています。(機種によって右後輪の取り外しが困難な場合があります)\nメーカーから部品だけの購入が不可と言われたため、自分で作成したものを出品しています。\n実績多数ありますが、購入後のトラブルには責任を負えません。ご了承いただける方のみご購入下さい。\n最近、ご購入者様からお褒めの言葉を多く頂いております。モチベーションの向上に繋がりますので、評価の方にもコメントいただけたら幸いです。")
   # 販売価格
   inputElement3 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[2].find_element_by_css_selector("input")
   inputElement3.send_keys("500")
def itm6(): #ダイソン掃除機 タイヤ2個+テフロンテープセット
   # 画像をアップロード
   driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/masa/Pictures/dyson/tire2set.JPG \n /Users/masa/Pictures/dyson/tire2.jpeg \n /Users/masa/Pictures/dyson/tape.jpeg \n /Users/masa/Pictures/dyson/moeterhead.jpeg \n /Users/masa/Pictures/dyson/morterheadback.jpeg")
   # 商品名
   inputElement1 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[0].find_element_by_css_selector("input")
   inputElement1.send_keys("ダイソン掃除機 タイヤ2個+テフロンテープセット")
   # 商品の説明
   inputElement1 = driver.find_elements_by_class_name("style_body__1OP1S")[2].find_element_by_css_selector("textarea")
   inputElement1.send_keys("\
   【商品紹介】\n画像の2～3枚目が商品になります。ダイソンモーターヘッドの裏側に付いているタイヤです。\nタイヤが劣化すると約１年ほどでフローリングや畳が傷つくことがあります。そのため、定期的に交換する必要があります。\
   \n\n【交換方法】\n交換方法などブログで詳しく紹介していますので、必ず購入前にご確認ください。\nブラウザでURLを入力すると検索できます。(URL：fuku-channnel.com)\nブログが検索できたら、サイト内検索で「ダイソン」と入力下さい。\
   \n\n【対象機種】\n実績機種は、DC35, DC48, DC59, DC62, V6です。\nその他の機種でも適合する可能性があります。(その他の機種でタイヤ交換をご検討されている方は次の保証内容をご確認ください。)\
   \n\n【保証内容】\n対象機種以外で交換をご検討されている場合、下記2点をご対応いただくことで保証が適応されることがあります。(対象機種は保証が適用されます)\n1. コメントにてご利用の機種をご連絡ください。\n2. ヘッドの裏の写真(タイヤ部分がわかる写真)を出品下さい。(価格は9,999,999としてください。)\nこちらで取り付けできると判断した場合のみ、保証が適応されます。保証が適応された場合、万が一取り付けできなかったら返金いたしますので、その旨ご連絡ください。\
   \n\n【交換頻度】\n１年以内の交換をおすすめしています。\n【タイヤのサイズ】\n外径: 10 mm\n内径: 3 mm\n幅: 4 mm\nシャフトにシールを巻くことを前提にしています。詳しくは上記ブログ（タイヤの取り付け方）をご覧下さい。\
   \n\n【現状のメーカー修理】\nメーカーで修理依頼すると、購入から2年以上経過すると最低5000円の工賃が発生します。\
   \n\n【最後に】\nタイヤは簡単に交換できるので、DIYで行うことをおすすめしています。(機種によって右後輪の取り外しが困難な場合があります)\nメーカーから部品だけの購入が不可と言われたため、自分で作成したものを出品しています。\n実績多数ありますが、購入後のトラブルには責任を負えません。ご了承いただける方のみご購入下さい。\n最近、ご購入者様からお褒めの言葉を多く頂いております。モチベーションの向上に繋がりますので、評価の方にもコメントいただけたら幸いです。")
   # 販売価格
   inputElement3 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[2].find_element_by_css_selector("input")
   inputElement3.send_keys("400")
def itm7(): #ダイソン掃除機 タイヤ2個
   # 画像をアップロード
   driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/masa/Pictures/dyson/tireimage.png \n /Users/masa/Pictures/dyson/tire2.jpeg \n /Users/masa/Pictures/dyson/moeterhead.jpeg \n /Users/masa/Pictures/dyson/morterheadback.jpeg")
   # 商品名
   inputElement1 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[0].find_element_by_css_selector("input")
   inputElement1.send_keys("ダイソン掃除機 タイヤ2個")
   # 商品の説明
   inputElement1 = driver.find_elements_by_class_name("style_body__1OP1S")[2].find_element_by_css_selector("textarea")
   inputElement1.send_keys("\
   【商品紹介】\n画像の2枚目が商品になります。ダイソンモーターヘッドの裏側に付いているタイヤです。\nタイヤが劣化すると約１年ほどでフローリングや畳が傷つくことがあります。そのため、定期的に交換する必要があります。\
   \n\n【交換方法】\n交換方法などブログで詳しく紹介していますので、必ず購入前にご確認ください。\nブラウザでURLを入力すると検索できます。(URL：fuku-channnel.com)\nブログが検索できたら、サイト内検索で「ダイソン」と入力下さい。\
   \n\n【対象機種】\n実績機種は、DC35, DC48, DC59, DC62, V6です。\nその他の機種でも適合する可能性があります。(その他の機種でタイヤ交換をご検討されている方は次の保証内容をご確認ください。)\
   \n\n【保証内容】\n対象機種以外で交換をご検討されている場合、下記2点をご対応いただくことで保証が適応されることがあります。(対象機種は保証が適用されます)\n1. コメントにてご利用の機種をご連絡ください。\n2. ヘッドの裏の写真(タイヤ部分がわかる写真)を出品下さい。(価格は9,999,999としてください。)\nこちらで取り付けできると判断した場合のみ、保証が適応されます。保証が適応された場合、万が一取り付けできなかったら返金いたしますので、その旨ご連絡ください。\
   \n\n【交換頻度】\n１年以内の交換をおすすめしています。\n【タイヤのサイズ】\n外径: 10 mm\n内径: 3 mm\n幅: 4 mm\nシャフトにシールを巻くことを前提にしています。詳しくは上記ブログ（タイヤの取り付け方）をご覧下さい。\
   \n\n【現状のメーカー修理】\nメーカーで修理依頼すると、購入から2年以上経過すると最低5000円の工賃が発生します。\
   \n\n【最後に】\nタイヤは簡単に交換できるので、DIYで行うことをおすすめしています。(機種によって右後輪の取り外しが困難な場合があります)\nメーカーから部品だけの購入が不可と言われたため、自分で作成したものを出品しています。\n実績多数ありますが、購入後のトラブルには責任を負えません。ご了承いただける方のみご購入下さい。\n最近、ご購入者様からお褒めの言葉を多く頂いております。モチベーションの向上に繋がりますので、評価の方にもコメントいただけたら幸いです。")
   # 販売価格
   inputElement3 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[2].find_element_by_css_selector("input")
   inputElement3.send_keys("300")
def itm8(): #トルクスドライバー3本セット（T10 & T8 & T6）
   # 画像をアップロード
   driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/masa/Pictures/torx/torxdriver.jpeg")
   # 商品名
   inputElement1 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[0].find_element_by_css_selector("input")
   inputElement1.send_keys("トルクスドライバー3本セット（T10 & T8 & T6）")
   # 商品の説明
   inputElement1 = driver.find_elements_by_class_name("style_body__1OP1S")[2].find_element_by_css_selector("textarea")
   inputElement1.send_keys("トルクスドライバー3本セット（T10 & T8 & T6）\
   \n\n ダイソン分解清掃などにお得な3本セットです。")
   # 販売価格
   inputElement3 = driver.find_elements_by_class_name("style_inputarea__1mtsA")[2].find_element_by_css_selector("input")
   inputElement3.send_keys("460")
# Open web (account 1)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 3'))
driver = webdriver.Chrome(options=options)

# メルカリのページにアクセス
sleep(1)
driver.get("https://www.mercari.com/jp/mypage/listings/listing/")
sleep(1)
# 出品中の商品リストを作成
itmlists = driver.find_elements_by_class_name("mypage-item-text")
lists = []
for itmlist in itmlists:
   lists.append(itmlist.text)
if not "ダイソン掃除機 タイヤ4個+テフロンテープ+トルクスドライバー３本セット" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm1()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ4個+テフロンテープ+シャフト4本セット" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm2()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ4個+テフロンテープ+シャフト4本+トルクスドライバー3本" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm3()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ4個+テフロンテープセット" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm4()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ4個" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm5()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ2個+テフロンテープセット" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm6()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ2個" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm7()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "トルクスドライバー3本セット（T10 & T8 & T6）" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm8()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
#全てのウインドウを閉じる
driver.quit()

# Open web (account 2)
options = webdriver.ChromeOptions()
options.add_argument(
   '--user-data-dir={chrom_dir_path}'.format(chrom_dir_path = '/Users/masa/Library/Application Support/Google/Chrome/Profile 2'))
driver = webdriver.Chrome(options=options)

# メルカリのページにアクセス
sleep(1)
driver.get("https://www.mercari.com/jp/mypage/listings/listing/")
sleep(1)
# 出品中の商品リストを作成
itmlists = driver.find_elements_by_class_name("mypage-item-text")
lists = []
for itmlist in itmlists:
   lists.append(itmlist.text)
if not "ダイソン掃除機 タイヤ4個+テフロンテープ+トルクスドライバー３本セット" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm1()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ4個+テフロンテープ+シャフト4本セット" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm2()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ4個+テフロンテープ+シャフト4本+トルクスドライバー3本" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm3()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ4個+テフロンテープセット" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm4()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ4個" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm5()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ2個+テフロンテープセット" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm6()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "ダイソン掃除機 タイヤ2個" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm7()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
if not "トルクスドライバー3本セット（T10 & T8 & T6）" in lists:
   sleep(1)
   driver.get("https://www.mercari.com/jp/sell/")
   sleep(1)
   # 画像をアップロード & 商品名 & 商品説明 & 販売価格
   itm8()
   # カテゴリ & ブランド
   ctd()
   # 商品の状態 & 配送料の負担 & 配送の方法 & 発送元の地域 & 発送までの日数
   mc()
   # 出品する
   sl = driver.find_element_by_css_selector("button[type=submit")
   sleep(1)
   #sl.click()
#全てのウインドウを閉じる
driver.quit()