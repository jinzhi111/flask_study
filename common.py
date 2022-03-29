# @Time : 2022-03-29 15:05 
# @Author : 金枝

import mysql_connect


def mysql_db():
    mysql = mysql_connect.MySql(host='localhost', user='root', password='root')
    return mysql


def user_data():
    # 先把用户数据查出来转化成字典类型
    mysql = mysql_db()
    user = mysql.select('SELECT *FROM flask_study.flask_user')  # 查询出来的数据是一个列表
    num = len(user)
    user_dict = {}
    for i in range(num):
        name = user[i]['username']
        psd = user[i]['password']
        user_dict[name] = psd
    return user_dict


if __name__ == '__main__':
    print(user_data())