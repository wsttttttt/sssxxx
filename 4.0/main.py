from flask import Flask, request
import requests
import menu
import sqlite3
import time
import re
import random
import os

app = Flask(__name__)


class API:
    @staticmethod
    def send(message):
        data = request.get_json()
        message_type = data['message_type']
        if 'group' == message_type:
            group_id = data['group_id']
            params = {
                "message_type": message_type,
                "group_id": str(group_id),
                "message": message
            }
        else:
            user_id = data['user_id']
            params = {
                "message_type": message_type,
                "user_id": user_id,
                "message": message
            }
        url = "http://127.0.0.1:5700/send_msg"

        requests.get(url, params=params)
    @staticmethod
    def selfsend(message):
        data = request.get_json()
        message_type = data['message_type']
    
        user_id = data['user_id']
        params = {
                "message_type":'private',
                "user_id": user_id,
                "message": message
            }
        url = "http://127.0.0.1:5700/send_msg"

        requests.get(url, params=params)
    @staticmethod
    def titi():
        data=request.get_json()
        message_type = data['message_type']
        group_id = data['group_id']
        user_id = data['user_id']
        post_data = {
                "group_id": str(group_id),
                "user_id": user_id
            }
        url = "http://127.0.0.1:5700/set_group_kick"
        requests.get(url, params=post_data)
        
    @staticmethod
    def setu(): 
        key = ''
        url = 'https://api.lolicon.app/setu?apikey=' + key + r'&size1200=true'
        menu = requests.get(url)
        setu_url = menu.json()['data'][0]['url'] # 对传回来的涩图网址进行数据提取
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:image,'r' file=' + str(setu_url) + r']'))
        #API.send( r'[CQ:image,'r' file=' + str(setu_url) + r']')

    @staticmethod
    def save_message():
        data = request.get_json()
        uid = data['user_id']
        message = data['message']
        message_id = data['message_id']
        send_time = data['time']
        message_type = data['message_type']
        raw_message=data['raw_message']
        if message_type == 'group':
            group_id = data['group_id']
        else:
            group_id = "无"
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        c.execute(
            "insert into message(QQ, message, message_id, send_time, message_type, group_id,raw_message) values (?, ?, ?, ?, ?, ?,?)",
            (uid, message, message_id, send_time, message_type, group_id,raw_message))
        conn.commit()
        conn.close()
    @staticmethod
    def lrs():
        
        
        print(da)
    @staticmethod
    def reply(message_id):
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        c.execute("SELECT * FROM message WHERE message_id = ?", (message_id,))
        results = c.fetchone()
        QQ = results[1]
        ID = results[0]
        group_id = results[6]
        message_type = results[5]
        num = ID + 1
        n = 0
        for i in range(60):
            n += 1
            try:
                c.execute("SELECT * FROM message WHERE id = ?", (num,))
                results = c.fetchone()
                new_QQ = results[1]
                new_group_id = results[6]
                new_message_type = results[5]
                if message_type == new_message_type == 'group':
                    if int(new_QQ) == int(QQ):
                        if int(new_group_id) == int(group_id):
                            new_message = results[2]
                            conn.commit()
                            conn.close()
                            return new_message
                        else:
                            num += 1
                            if n == 58:
                                conn.commit()
                                conn.close()
                                return "回复超时"
                            else:
                                time.sleep(1)
                                continue
                    else:
                        num += 1
                        if n == 58:
                            conn.commit()
                            conn.close()
                            return "回复超时"
                        else:
                            time.sleep(1)
                            continue
                elif message_type == new_message_type == 'private':
                    if int(new_QQ) == int(QQ):
                        new_message = results[2]
                        conn.commit()
                        conn.close()
                        return new_message
                    else:
                        num += 1
                        if n == 58:
                            conn.commit()
                            conn.close()
                            return "回复超时"
                        else:
                            time.sleep(1)
                            continue
                else:
                    num += 1
                    if n == 58:
                        conn.commit()
                        conn.close()
                        return "回复超时"
                    else:
                        time.sleep(1)
                        continue
            except:
                if n == 58:
                    conn.commit()
                    conn.close()
                    return "回复超时"
                else:
                    time.sleep(1)
                    continue


@app.route('/', methods=["POST"])
def post_data():
    """下面的request.get_json().get"""
    data = request.get_json()
    print(data)
    
    if data['post_type'] == 'message':
        API.save_message()
        message = data['message']
        print(message)
    
    
        menu.menu()
    else:
        print("暂不处理")

    return "OK"


if __name__ == '__main__':
    # 此处的 host和 port对应上面 yml文件的设置
    app.run(host='0.0.0.0', port=5703)  
