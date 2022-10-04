from flask import Flask, request
import requests     #申请http,响应正文
import menu


app = Flask(__name__)


class API:
    @staticmethod#Pyhonz中的静态方法，据说很方便
    def send(message):
        url = "http://127.0.0.1:5700/send_msg"
        data = request.get_json()
        message_type=data['message_type']
        if 'group'==message_type:
            group_id=data['group_id']
            params = {
             "message_type": message_type,
             "group_id": str(group_id),
             "message": message
            }
        else:
            user_id=data['user_id']
            params = {
            "message_type": message_type,
            "user_id": str(user_id),
            "message": message
            }     
                
        
      
        requests.get(url, params=params)


@app.route('/', methods=["POST"])#使程序运行
def post_data():
    """下面的request.get_json().get......是用来获取关键字的值用的"""
    data = request.get_json()
    print(data)
    if data['post_type'] == 'message':
        message = data['message']
        print(message)
        menu.menu()
    else:
        print("暂不处理")
        
    return "OK"


if __name__ == '__main__':
    # 此处的 host和 port对应上面 yml文件的设置
    app.run(host='0.0.0.0', port=5703)  # 保证和我们在配置里填的一致
