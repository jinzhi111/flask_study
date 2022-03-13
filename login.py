# @Time : 2022-03-13 22:12 
# @Author : 金枝
from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/login', methods=['get','post'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    if name == 'jinzhi' and password == '123456':
        return '登录成功'
    else:
        return '登录失败'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
