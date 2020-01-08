# -*- coding: utf-8 -*-
import socket
import time
from threading import *
from Tkinter import *
import random

global client_sock2, client_sock1
ip = '127.0.0.1'
port = 7777
client_sock1 = ' '
client_sock2 = ' '
name1 = ' '
name2 = ' '
gamestart=0
word1 ='a'
word2 = 'a'
dictque1 = {1: '후라이드 vs 양념', 2: '부먹 vs 찍먹', 3:'짜장면 vs 짬뽕', 4:'오버워치 vs 롤', 5:'여름 vs 겨울',
            6:'수학 vs 영어', 7:'산 vs 바다', 8:'피자 vs 치킨', 9:'야구 vs 농구', 10:'사탕 vs 초콜릿',
            11:'단발 vs 장발', 12:'맥주 vs 소주', 13:'호랑이 vs 사자', 14:'돼지고기 vs 소고기', 15:'안경 vs 렌즈',
            16:'귀여움 vs 섹시함', 17:'아이폰 vs 갤럭시', 18:'미국 vs 유럽', 19:'떡볶이 vs 순대', 20:'커피 vs 코코아',
            21:'딸기우유 vs 바나나우유', 22:'밥 vs 빵', 23:'카레 vs 짜장', 24:'과자 vs 아이스크림',
            25:'과일쥬스 vs 탄산음료', 26:'캐주얼 vs 정장', 27:'청바지 vs 면바지', 28:'귀걸이 vs 목걸이',
            29:'샌들 vs 운동화', 30:'가요 vs 팝송', 31:'흰색 vs 검은색', 32:'피씨방 vs 노래방', 33:'비빔밥 vs 볶음밥'}

class subApp:
    def __init__(self, Master):
        self.master = Master
        Master.title("서버 구축")
        Master.geometry("200x100")
        self.submainFrame = Frame(self.master)
        self.submainFrame.pack(fill=X)
        self.label1 = Label(self.submainFrame, text="서버 열기")
        self.label1.pack(side=TOP)

        self.submainFrame1 = Frame(self.master)
        self.submainFrame1.pack(fill=X)
        self.submainFrame2 = Frame(self.master)
        self.submainFrame2.pack(fill=X)
        self.submainFrame3 = Frame(self.master)
        self.submainFrame3.pack(fill=X)

        self.label1 = Label(self.submainFrame1, text="server ip")
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(self.submainFrame1, bd=1, width=10)
        self.entry1.pack(side=LEFT)
        self.label2 = Label(self.submainFrame2, text="server port")
        self.label2.pack(side=LEFT)
        self.entry2 = Entry(self.submainFrame2, bd=1, width=5)
        self.entry2.pack(side=LEFT)
        self.button = Button(self.submainFrame3, text="연결", height=2, command=self.openserver)
        self.button.pack(side=TOP)

    def openserver(self):
        global ip, port
        ip = self.entry1.get()
        port = int(self.entry2.get())
        self.master.quit()
        self.master.destroy()

root = Tk()
app = subApp(root)
root.mainloop()
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(ip, port)
server_sock.bind((ip, port))
server_sock.listen(2)
count = 0
connection = 0

def socket1():
    global client1, addr1, name1, count, connection
    count += 1
    client1, addr1 = server_sock.accept()
    print("[알림] :" + str(addr1[1]) + " 연결")
    connection += 1
    name1 = client1.recv(65535)
    sendmessage("[System]", name1 + "님이 입장하셨습니다.")
    while True:
        data1 = client1.recv(65535)
        if data1 == '@':
            break
        elif data1 == '+':
            gamemessage1(data1)
        elif data1 == '*':
            gamemessage2(data1)
        else:
            sendmessage(name1, data1)
    sendmessage("[System]", name1 + "님이 나가셨습니다.")
    count -= 1
    connection -= 1
    client1.close()

def socket2():
    global client2, addr2, name2, count, connection
    count += 2
    client2, addr2 = server_sock.accept()
    print("[알림] :" + str(addr2[1]) + " 연결")
    connection += 2
    name2 = client2.recv(65535)
    sendmessage("[System]", name2 + "님이 입장하셨습니다.")
    while True:
        data2 = client2.recv(65535)
        if data2 == '@':
            break
        elif data2 == '-':
            gamemessage1(data2)
        elif data2 == '/':
            gamemessage2(data2)
        else:
            sendmessage(name2, data2)
    sendmessage("[System]", name2 + "님이 나가셨습니다.")
    count -= 2
    connection -= 2
    client2.close()

def sendmessage(name, data):
    message = name + " : " + data
    print(message)
    if connection == 1:
        client1.send(message)
    if connection == 2:
        client2.send(message)
    if connection == 3:
        client1.send(message)
        client2.send(message)

def gamemessage1(data):
    global gamestart, word1, word2
    gamestart=0
    word1 = 'a'
    word2 = 'a'
    if data == '+':
        sendmessage("[System]", name1 + "님이 끝말잇기에 들어오셨습니다.")
    elif data == '-':
        sendmessage("[System]", name2 + "님이 끝말잇기에 들어오셨습니다.")
    while True:
        if data=='+':
            data1 = client1.recv(65535)
            if gamestart == 1:
                break
            sendmessage(name1, data1.strip('\n') + "     (패배선언 : GG버튼 클릭)")
            if data1 == 'gg':
                sendmessage("[System]", name2 + "님이 끝말잇기를 이겼습니다.")
                gamestart = 1
                break
            word1 = str(data1)
            if (word2 != 'a') and (word1[0] != word2[-2]):
                sendmessage("[System]", "단어가 틀렸습니다. "+name2 + "님이 끝말잇기를 이겼습니다.")
                gamestart = 1
                break
        elif data=='-':
            data2 = client2.recv(65535)
            if gamestart == 1:
                break
            sendmessage(name2, data2.strip('\n') + "     (패배선언 : GG버튼 클릭)")
            if data2=='gg' :
                sendmessage("[System]", name1 + "님이 끝말잇기를 이겼습니다.")
                gamestart = 1
                break
            word2 = str(data2)
            if (word1 != 'a') and (word2[0] != word1[-2]):
                sendmessage("[System]", "단어가 틀렸습니다. "+name1 + "님이 끝말잇기를 이겼습니다.")
                gamestart = 1
                break

def gamemessage2(data):
    num = random.randint(1, 33)
    sendmessage("[System]", dictque1[num])
    if data=='*':
        data1 = client1.recv(65535)
        sendmessage("[System]", name1 + "님은 " + data1.strip('\n') + "을(를) 선택하셨습니다")
    elif data=='/':
        data2 = client2.recv(65535)
        sendmessage("[System]", name2 + "님은 " + data2.strip('\n') + "을(를) 선택하셨습니다")

sock1 = Thread(target=socket1)
sock2 = Thread(target=socket2)
sock1.start()
sock2.start()