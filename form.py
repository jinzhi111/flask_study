# @Time : 2022-03-22 13:43 
# @Author : 金枝

from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Length, Regexp  # 验证数据不能为空


# 定义表单模型类
class Register(FlaskForm):
    """
    validators:验证器
    Regexp:正则表达式
    render_kw:前端样式
    placeholder:提示语

    """
    username = StringField(label='用户名',
                           validators=[DataRequired(u'用户名不能为空'), Length(min=8, max=8, message='用户名长度必须是8位'),
                                       Regexp(regex=r'^\S+\w{6}\S{1,}', message='用户名不可以有特殊字符和空格')],
                           render_kw={"class": "form-control", "placeholder": "请输入用户名", "required": 'required'})
    password = PasswordField(label='密码', validators=[DataRequired(u'密码不能为空'), Length(min=5, message='密码长度必须大于5位'),
                                                     Regexp(regex=r'^[A-Za-z0-9]+$', message='密码只能是字母和数字组合')],
                             render_kw={"class": "form-control", "placeholder": "请输入密码", "required": 'required'})
    password2 = PasswordField(label='密码确认', validators=[DataRequired(u'密码不能为空'), EqualTo('password', '两次密码不相同')],
                              render_kw={"class": "form-control", "placeholder": "请再次输入密码", "required": 'required'})
    submit = SubmitField(label='注册')

    def validate_name(self,field):
        pass