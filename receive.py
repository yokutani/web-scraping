from selenium import webdriver
from selenium.webdriver.common.by import By
import functions

#GigaCCにログイン
def receive():
    url = 'https://asp.gigacc.com/user/'
    LoginId = 'アドレス'
    password = 'パスワード'
    driver = webdriver.Chrome(executable_path='C:\\Users\\yoshiki\\Downloads\\chromedriver_win32\\chromedriver.exe')

    driver.get(url)
    driver.implicitly_wait(10)
    login_box = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/dl/dd[1]/input[1]')
    login_box.send_keys(LoginId)
    password_box = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/dl/dd[2]/input')
    password_box.send_keys(password)
    lg_botton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/p/input[2]')
    lg_botton.click()

    #二重ログイン時の強制ログイン
    cur_url = driver.current_url
    if cur_url == 'https://asp.gigacc.com/user/user/authentication.do':
        #ログインするクリック
        lg2_botton = driver.find_element_by_xpath('/html/body/div[1]/div/form/p/input[1]')
        lg2_botton.click()

    #ここからnew_message
    #受信箱クリック
    jusinbox_botton = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[1]/div[1]/ul/li[3]/a')
    jusinbox_botton.click()

    #受信箱の中身を表示
    jusin_table = driver.find_element_by_class_name('tbl_fixed')
    jusin_tr = jusin_table.find_elements(By.TAG_NAME, "tr")
    for i in range(1, len(jusin_tr)):
        jusin_td = jusin_tr[i].find_elements(By.TAG_NAME, "td")
        line = str(i) + " "
        line += "%s\t\t" % (jusin_td[1].text)
        line += "%s\t\t" % (jusin_td[2].text)
        line += "%s" % (jusin_td[4].text)
        line = functions.receive_newline_to_space(line)
        print (line)

    #開きたいメールを選択
    while (1):
        j = input('上記から開くメールを1~' + str(i) + 'で選択してください。\n>>')
        if functions.receive_check_num(j) == 1:
            j = int(j)
            if 1 <= j <= i:
                break
    newmessage_botton = driver.find_element_by_xpath('/html/body/div[3]/div/form[2]/table/tbody/tr[' + str(j) + ']/td[9]/a')
    newmessage_botton.click()

    #メールの本文表示
    Text = driver.find_element_by_xpath('/html/body/div[3]/div/table/tbody/tr[9]/td/p')
    print(Text.text)

    #ファイルのダウンロード
    #圧縮してダウンロードボタンのxpath
    zip_button = driver.find_elements_by_xpath('/html/body/div[3]/div/table/tbody/tr[7]/td/input[2]')
    if len(zip_button) != 0:
        zip_button[0].click()
    #圧縮ダウンロードがなかった際のダウンロードボタンの押下
    else:
        file = driver.find_element_by_xpath('/html/body/div[3]/div/table/tbody/tr[7]/td/input[1]')
        file.click()
