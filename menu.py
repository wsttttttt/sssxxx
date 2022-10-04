from flask import Flask, request
import requests
from main import API


def menu():
    data=request.get_json()
    message=data['message']

    if "菜单"==message:
        a="""
        你可以和我说
        1.你好
        2.你不好
        """
        API.send(a)
    elif"你好"==message:
        a='你也好呀'

        API.send(a)
    else:
        a='滚！！'
        API.send(a)
    return"OK"
    
    
