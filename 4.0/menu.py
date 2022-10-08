from flask import Flask, request
import requests
from main import API
import re
import random
import os

def menu():
    data = request.get_json()
    message = data['message']
    message_id = data['message_id']
    message_type = data['message_type']
    uid = data['user_id'] 
    if "hey bot" == message:
        a = "我在哦"
        API.send(a)
    elif "你好" == message:
        a = '你也好啊'
        API.send(a)
    elif '色图' == message:
        API.send("请输入你的XP")
        messages = API.reply(message_id)
        '''rand=random.randint (1,4)'''
        if "超时" in messages:
            if message_type == 'group':
                API.send("[CQ:at,qq="+str(uid)+"]"+"回复超时")
            else:
                API.send("回复超时")
        elif '萝莉'==messages:
            rand=random.randint(1,2)
            if rand==1:
                API.send("喜欢" + str(messages)+"太刑了")
                a='[CQ:image,file=ea0c0490e8e20892553abee9fea6f5e8.image,url=https://c2cpicdw.qpic.cn/offpic_new/2963224321//2963224321-1096522084-EA0C0490E8E20892553ABEE9FEA6F5E8/0?term=3]'
                API.send(a)
            elif rand==2:
                API.send("喜欢" + str(messages)+"太刑了")
                a='[CQ:image,file=c610473ef653f78e15ccdc4247be7aab.image,url=https://c2cpicdw.qpic.cn/offpic_new/2963224321//2963224321-4160077348-C610473EF653F78E15CCDC4247BE7AAB/0?term=3]'
                API.send(a)
        elif'御姐'==messages:
            API.send("XP不错，喜欢" + str(messages))
            a='[CQ:image,file=60175f82b9591bc13db9d914aa3dc11a.image,url=https://c2cpicdw.qpic.cn/offpic_new/2963224321//2963224321-1274617754-60175F82B9591BC13DB9D914AA3DC11A/0?term=3]'
            API.send(a)
        elif'我是男同'==messages:
            API.send("你个男同，拿了快走" )
            a='[CQ:image,file=9a78d3d7b4f642de9622b76707b7701a.image,url=https://c2cpicdw.qpic.cn/offpic_new/2963224321//2963224321-1670389562-9A78D3D7B4F642DE9622B76707B7701A/0?term=3]'
            API.send(a)
        else:
            API.send("你的XP好奇怪,竟然喜欢"+str(messages)+"，给你这个")
            a='[CQ:image,file=cfedaab9a0b861d40fe48a9810106f42.image,url=https://c2cpicdw.qpic.cn/offpic_new/2963224321//2963224321-4237709381-CFEDAAB9A0B861D40FE48A9810106F42/0?term=3]'
            API.send(a)
    elif '看猫猫狗狗' == message:
        API.send("到底是猫猫还是狗狗")
        messages = API.reply(message_id)
        '''rand=random.randint (1,4)'''
        if "超时" in messages:
            if message_type == 'group':
                API.send("[CQ:at,qq="+str(uid)+"]"+"回复超时")
            else:
                API.send("回复超时")
        elif '猫猫'==messages:
            API.send("给你" + str(messages))
            a='[CQ:image,file=3c1a1e02d9a1d838ca63b6e094bf135c.image,url=https://c2cpicdw.qpic.cn/offpic_new/2963224321//2963224321-3750517559-3C1A1E02D9A1D838CA63B6E094BF135C/0?term=3]'
            API.send(a)
        elif'狗狗'==messages:
            rand=random.randint(1,2)
            if rand==1:
               API.send("XP不错，喜欢" + str(messages))
               a='[CQ:image,file=e5a386174a0ee22542be125b9197cc17.image,url=https://c2cpicdw.qpic.cn/offpic_new/2963224321//2963224321-1476962004-E5A386174A0EE22542BE125B9197CC17/0?term=3]'
               API.send(a)
            elif rand==2:
               API.send("XP不错，喜欢" + str(messages))
               a='[CQ:image,file=5714cbd83b3180ce7a43e7bbe725e1df.image,url=https://c2cpicdw.qpic.cn/offpic_new/2963224321//2963224321-3469337769-5714CBD83B3180CE7A43E7BBE725E1DF/0?term=3]'
               API.send(a)
               
    elif'踢我'==message:
        API.titi()
        
    elif'你妈'==message:
        API.titi()
        
    elif'滚'==message:
        API.titi()
        
    elif'nmsl'==message:
        API.titi()
  
    elif'狼人杀'==message:
            API.send('是否加入游戏')
            messages = API.reply(message_id)
            
            if'加入'==messages:
                rand=random.randint(1,4)
                if rand==1:
                   API.selfsend('平民')
                elif rand==2:
                   API.selfsend('平民')
                elif rand==3:
                   API.selfsend('平民')    
                elif rand==4:
                   API.selfsend('狼人')
            elif'不加入'==messages:
                API.send('看你的色图去吧')
    return "OK"
