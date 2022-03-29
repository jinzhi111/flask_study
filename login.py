# @Time : 2022-03-13 22:12 
# @Author : 金枝
import time

from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect

from common import *
from form import *

app = Flask(__name__, template_folder='templates')
# 给程序添加上任意字符串，因为程序有机制保护代码不被随意访问
app.config['SECRET_KEY'] = 'shdhgfg'


@app.route('/', methods=['GET', 'POST'])
def index():
    # 创建表单对象
    user_dict = user_data()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            if user_dict[username] == password:
                return '登录成功'
            else:
                return render_template('index.html', login_status=0)
        except KeyError:
            # login_status = 1

            # return redirect(url_for('register'))
            return render_template('index.html', login_status=1)
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    user_dict = user_data()
    form = Register()
    if request.method == 'POST':
        # 走自定义表单验证
        username = form.username.data
        password = form.password.data
        password2 = form.password2.data
        if username in user_dict.keys():
            flash('用户已存在，请重新填写注册名')
        else:
            if form.validate_on_submit():
                mysql = mysql_db()
                # "{username}","{password}" 这个双引号必须加，不然数据库插数据会报错
                mysql.insert(f'INSERT INTO flask_study.flask_user (username,password)VALUES("{username}","{password}")')
                return render_template('register.html', form=form, register_status=1)
                # flash('注册成功')
                # return redirect(url_for('index'))
            else:
                return render_template('register.html', form=form)
    return render_template('register.html', form=form)


@app.route('/reset_pwd', methods=['GET', 'POST'])
def reset_pwd():
    user_dict = user_data()
    form = ResetPwd()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        if username not in user_dict.keys():
            flash('需要修改密码的账号不存在，请输入正确账号')
        else:
            if form.validate_on_submit():
                mysql = mysql_db()
                mysql.updata(f'UPDATE flask_study.flask_user SET PASSWORD = "{password}" WHERE username = "{username}"')
                return render_template('reset_pwd.html', form=form, reset_status=1)
            else:
                return render_template('reset_pwd.html', form=form)
    return render_template('reset_pwd.html', form=form)



# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         repassword = request.form.get('repassword')
#         if password == repassword:
#             if username not in user.keys():
#                 user[username] = password
#                 return redirect(url_for('index'))
#             else:
#                 return '账号已注册，请直接登录'
#         else:
#             return '两次密码不相同，请重新输入'
#     return render_template('register1.html')


if __name__ == '__main__':
    app.run(debug=True)
