from selenium import webdriver
import functions
def send():
    #送信先の選択
    send_list = functions.send_select_members()
    #名前・件名・本文の入力
    send_str = functions.send_input_str()
    #ファイルの選択
    send_file = functions.send_select_file()
    #ドライバーの取得
    driver = webdriver.Chrome(executable_path='C:\\Users\\yoshiki\\Downloads\\chromedriver_win32\\chromedriver.exe')
    i = 0
    while i < len(send_list):
        driver.implicitly_wait(100)
        driver.get(send_list[i])
        #名前・件名・本文の入力
        name_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/table/tbody/tr[2]/td/input')
        name_box.send_keys(send_str[0])
        title_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/table/tbody/tr[3]/td/input')
        title_box.clear()
        title_box.send_keys(send_str[1])
        message_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/table/tbody/tr[6]/td/textarea')
        message_box.send_keys(send_str[2])
        #ファイルの入力
        n = len(send_file) - 1
        while n >= 0:
            file_upload = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/table/tbody/tr[5]/td/div[1]/input')
            file_upload.send_keys(send_file[n])
            n -= 1
        #送信ボタンの押下
        send_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/p/input[1]')
        send_button.click()
        end = driver.find_element_by_xpath('/html/body/div[2]/p/input')
        end.click()
        i += 1