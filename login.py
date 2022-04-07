# @Time : 2022-03-13 22:12 
# @Author : 金枝
import time
from datetime import timedelta

from flask import Flask, render_template, request, url_for, flash, session
from werkzeug.utils import redirect

from common import *
from form import *
from flask_login import login_required, current_user, LoginManager


app = Flask(__name__, template_folder='templates')
# 给程序添加上任意字符串，因为程序有机制保护代码不被随意访问
app.config['SECRET_KEY'] = 'shdhgfg'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)  # 设置session时间，30s过期


# login_manager = LoginManager(app)
# login_manager.init_app(app)  # 初始化
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'index'
#
# # 这个callback函数用于reload User object，根据session中存储的user id
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 创建表单对象
    user_dict = user_data()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            if user_dict[username] == password:
                session['username'] = username
                # return '登录成功'
                # 登录成功后返回上级页面
                next_page_url = request.args.get('next')
                # 如果 next_page_url 为空，直接返回首页
                if not next_page_url:  # or url_parse(next_page_url).netloc != ''
                    return redirect(url_for('setting'))
                else:
                    return redirect(next_page_url)
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


@app.route('/', methods=['GET', 'POST'])
def setting():
    # 判断用户是否登录，已登录直接进入首页
    if 'username' in session:
        return render_template('setting.html', name=session['username'])
    # 未登录跳转登录页面
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
