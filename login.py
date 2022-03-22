# @Time : 2022-03-13 22:12 
# @Author : 金枝
from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect

from form import Register
app = Flask(__name__, template_folder='templates')
# 给程序添加上任意字符串，因为程序有机制保护代码不被随意访问
app.config['SECRET_KEY'] = 'shdhgfg'

user = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    # 创建表单对象
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            if user[username] == password:
                return '登录成功'
            else:
                return render_template('index.html', login_status=0)
        except KeyError:
            # login_status = 1
            return redirect(url_for('register'))
            # return render_template('index.html', login_status=1)
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == 'POST':
        # 走自定义表单验证
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            password2 = form.password2.data
            user[username] = password
            print(user)
            return redirect(url_for('index'))
        else:
            flash('注册失败')
    return render_template('register.html', form=form)


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
    app.run()
