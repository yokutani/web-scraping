import send
import receive

while (1):
    i = input('受信:1  送信:2  終了:3\n>>')
    if i == '1':
        receive.receive()
    elif i == '2':
        send.send()
    elif i == '3':
        break
    else:
        continue
