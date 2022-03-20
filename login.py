# @Time : 2022-03-13 22:12 
# @Author : 金枝
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo  # 验证数据不能为空

app = Flask(__name__)
# 给程序添加上任意字符串，因为程序有机制保护代码不被随意访问
app.config['SECRET_KEY'] = 'shdhgfg'

user = {}


# 定义表单模型类
class Register(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码', validators=[DataRequired('密码不能为空')])
    password2 = PasswordField(label='再次输入密码', validators=[DataRequired('密码不能为空'), EqualTo('password')])
    submit = SubmitField(label='注册')


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
                return '登录失败'
        except KeyError:
            return redirect(url_for('register'))
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user[username]=password
        else:
            return '验证失败'
    return render_template('register.html', form=form)


# @app.route('/')


if __name__ == '__main__':
    app.run()
