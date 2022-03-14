# @Time : 2022-03-13 22:12 
# @Author : 金枝
from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo  # 验证数据不能为空

app = Flask(__name__)
# 给程序添加上任意字符串，因为程序有机制保护代码不被随意访问
app.config['SECRET_KEY'] = 'shdhgfg'
# 定义表单模型类
class Login(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
    password = StringField(label='密码', validators=[DataRequired('密码不能为空')])
    submit = SubmitField(label='提交')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 创建表单对象
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'jinzhi' and password == '123456':
            return '登录成功'
        else:
            return '登录失败'
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Login()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()
