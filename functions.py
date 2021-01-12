#送信側

#送信先選択
def send_select_members():
    #返信用URL
    member = {'adachi':'https://asp.gigacc.com/user/~th/nmkhj0cb7vr4j0ng2b9a7l8ttg', 'ito':'https://asp.gigacc.com/user/~th/qorc1736lmp1q1ga0itsus7esg', 'umemuro':'https://asp.gigacc.com/user/~th/kagbf3129k5ldem0a8dodf1rek', 'okutani':'https://asp.gigacc.com/user/~th/gcip5clqhpqr1hqjn4mim50ei8', 'kangori':'https://asp.gigacc.com/user/~th/j1ljeis660lsdbbhfl83ktrnrk', 'ka':'https://asp.gigacc.com/user/~th/qv9konotq317lv6t7fpu5sgfg4'}
    send_list = list(range(0))

    while (1):
        print('送信先を選択してください。')
        send = input('\'adachi\' \'ito\' \'umemuro\' \'okutani\' \'kangori\' \'ka\'\n>>')
        for member_key in member:   
            if member_key == send:          #入力されたものがmemberの配列にある時
                i = 0
                while i < len(send_list):   #すでにlistにないかを確認
                    if send_list[i] == member[member_key]:
                        break
                    i += 1
                if i == len(send_list):     #listになければlistに追加
                    print('\n送信先に\'' + send + '\'を追加しました。\n')
                    send_list.append(member[send])
                else:
                    print('\n' + send + 'はすでに選択されています。\n')
                break
        if len(send_list) == 0:             #listが0の時はもう一度選択
            print('送信先が選択されていません。')
            continue
        print('送信先を追加しますか？')
        add = input('追加する:y  追加しない:その他のキー\n>>')
        if add == 'y' or add == 'ｙ':
            continue
        break
    return send_list

#名前・件名・メッセージの入力
def send_input_str():
    while (1):
        name = input('\n名前を入力(30字以内)\n>>')
        if len(name) == 0:
            print('名前を入力してください。')
            continue
        elif len(name) <= 30:
            print(name + '(' + str(len(name)) + '字)' + '\nでよろしいですか？')
            if input('いいえ:n  はい:その他のキー\n>>') == 'n':
                continue
        else:
            print(str(len(name)) + '字です。もう一度入力してください。')
            continue
        break

    while (1):
        title = input('\n件名を入力(30字以内)\n>>')
        if len(title) == 0:
            title = '件名なし'
        if len(title) <= 30:
            print(title + '(' + str(len(title)) + '字)' + '\nでよろしいですか？')
            if input('いいえ:n  はい:その他のキー\n>>') == 'n':
                continue
        else:
            print(str(len(title)) + '字です。もう一度入力してください。')
            continue
        break

    while (1):
        message = input('本文を入力(1000字以内)\n>>')
        if len(message) <= 1000:
            print(message + '(' + str(len(message)) + '字)' + '\nでよろしいですか？')
            if input('いいえ:n  はい:その他のキー\n>>') == 'n':
                continue
        else:
            print(str(len(message)) + '字です。もう一度入力してください。')
            continue
        break
    str_list = list(message)
    temp_list = list(range(0))
    str_len = len(str_list)
    i = 0
    while i < str_len:
        if str_list[i] == '$':
            temp_list.append('\n')
            i += 1
        else:
            temp_list.append(str_list[i])
            i += 1
    message = ''.join(temp_list)
    send_str = [name, title, message]
    return send_str

#ファイルの選択
def send_select_file():
    path_changed = list(range(0))
    while (1):
        file_path = input('ファイルをコンソールにDrag and dropしてください:\n>>')
        str_list = list(file_path)
        list_len = len(str_list)
        
        i = 0
        count = 0
        
        while i < list_len:
            if str_list[i] == '\'':
                count += 1
            i += 1
            
        count /= 2
        i = 0
        
        #ファイルが2つ以上ドロップされた場合
        while count > 0: 
            count_s = 0
            temp_list = list(range(0))
            #ファイルのパス名を変更
            while i < list_len:
                if str_list[i] == '/':
                    temp_list.append('\\')
                    temp_list.append('\\')
                    i += 1
                if str_list[i] == '\'':
                    i += 1
                    count_s += 1
                    #「'」の２個目でループを脱出
                    if count_s == 2:
                        i += 2
                        break
                else:
                    temp_list.append(str_list[i])
                    i += 1
            path_changed.append(''.join(temp_list))
            count -= 1
        if len(path_changed) == 0:
            continue
        if input('ファイルを追加しますか？\nyes:y no:その他のキー\n>>') != 'y':
            break
    return path_changed


#受信側

#\nをスペースに置換
def receive_newline_to_space(str1):
    str_list = list(str1)
    i = 0
    while i < len(str_list):
        if str_list[i] == '\n':
            str_list[i] = ' '
        i += 1
    ptr = ''.join(str_list)
    return ptr

#文字列がすべて数字でできているか判別
def receive_check_num(str1):
    str_list = list(str1)
    if len(str_list) == 0:
        return (0)
    i = 0
    while i < len(str_list):
        if not '0' <= str_list[i] <= '9':
            return (0)
        i += 1
    return (1)