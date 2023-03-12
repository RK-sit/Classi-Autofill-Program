from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random

# Windowsで実行する場合は、ダウンロードしたChromeDriverを解凍し、「chromedriver.exe」を適当な場所に置いてください。
#そして、以下のように入力してChromeDriverを読み込みます
# （Macで実行する場合は以下をコメントアウトしてください）
#driver = webdriver.Chrome('ChromeDriverのディレクトリ + chromedriver')

# Windowsで実行する場合は以下のものをコメントアウトしてください
browser = webdriver.Chrome()

#以下にClassiのログインIDとパスワードを入力してください。
classi_login = 'ログインID'
classi_pass = 'パスワード'

url = 'https://sas.benesse.ne.jp/classi/s/'
browser.get(url)

name_form = browser.find_element_by_xpath('//*[@id="student_form"]/div/div[1]/input')
name_form.send_keys(classi_login)

pass_form = browser.find_element_by_xpath('//*[@id="usr_password"]')
pass_form.send_keys(classi_pass)  

login_button = browser.find_element_by_xpath('//*[@id="student_form"]/div/button')
login_button.click()

sleep(3)

enter = ['楽しい一日だった！', '今日は少し疲れた。', 'たくさんのことをやり遂げることができた。','家でのんびり過ごした。','部活で楽しいことがあった','部活で嬉しいことがあった','友達を作ることができました','今日は忙しい1日でした','面白いニュースを聞いてほんわかとした気持ちになった','外で運動する時間があった','1日寝ないで集中することができた','今日は暑かった','いい出会いがあった','ずっと前から楽しみにしていたことが実現しました！','新しいことを学べた','今日1日、忙しすぎた','今日は、大切な人と過ごすことができた','ずっと食べたかったアイスを食べることができた','理想と現実が合わなかった','アレルギーだったピーナッツを克服することができた','おじいちゃんにMacBookを買ってもらった','おばあちゃんにiPhoneを買ってもらった','ひいおじいちゃんにApple Watchを買ってもらった','ひいおばあちゃんにiPadを買ってもらった','ひいひいおじいちゃんにAirPods Proを買ってもらった','ひいひいおばあちゃんにAirTagをつけた','1000円無くした','今日はとても天気が良かった','久しぶりに部屋の片付けをした','駅のホームで、ｳｰﾀﾝ､ｹﾞﾞﾝｷ! ｹﾞﾝｷ!と叫んでいる男がいた']

#処理を行いたい年と月を入力してください
year = '2023'
month = '03'

#処理を行いたい月の日数から9を引いたものを入力してください。（例：1カ月が31日の場合は'22'、1ヶ月が30日の場合は'21'、1ヶ月が28日の場合は'19'）
day = 22

for i in range(9):
  number = len(enter)
  number2 = number - 1
  random_number = random.randint(0, number2)
  
  sleep(3)

  study_url = ('https://study.classi.jp/reports/form/'+ year + '-' + month + '-0' + str(i + 1))
  browser.get(study_url)
  
  sleep(3)
  
  texts = browser.find_element_by_xpath('/html/body/study-root/spen-single-column/div/main/study-my-report-form/form/div[2]/div[2]/study-student-message/div/div[2]/div/textarea')
  texts.clear()
  texts.send_keys((enter[random_number]))
  
  sleep(3)
  
  confirm_contents_button = browser.find_element_by_xpath('/html/body/study-root/spen-single-column/div/main/study-my-report-form/form/div[2]/div[3]/button')
  confirm_contents_button.click()
  
  sleep(3)

for i in range(day):

  number = len(enter)
  number2 = number - 1
  random_number2 = random.randint(0, number2)

  sleep(3)
  
  study_url = ('https://study.classi.jp/reports/form/'+ year + '-' + month + '-' + str(i + 10))
  browser.get(study_url)
  
  sleep(3)
  
  texts = browser.find_element_by_xpath('/html/body/study-root/spen-single-column/div/main/study-my-report-form/form/div[2]/div[2]/study-student-message/div/div[2]/div/textarea')
  texts.clear()
  texts.send_keys((enter[random_number]))
  
  sleep(3)
  
  confirm_contents_button = browser.find_element_by_xpath('/html/body/study-root/spen-single-column/div/main/study-my-report-form/form/div[2]/div[3]/button')
  confirm_contents_button.click()
  
  sleep(3)

  # ©️RK.2023-3-12pip listpip list